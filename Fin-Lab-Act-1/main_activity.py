import argparse
from multiprocessing.managers import BaseManager, ListProxy
import time
import threading

"""Master-worker MPI demo (minimal).

This file implements the activity requirements:
- Master generates 6 orders and starts a Manager server exposing a shared list and lock proxy.
- Master assigns orders round-robin to workers and sends manager address/authkey.
- Workers connect to manager, sleep to simulate processing, and append completed orders.
- Run with `--no-sync` to demonstrate race conditions, or `--sync` to protect writes with a lock.
"""

# manager class daw ni
class OrderManager(BaseManager):
    pass

# ang manager-side shared objects and functions daw ni nga magamit sa manager process ug ma-access sa worker processes through sa manager proxies
SHARED_ORDERS = []  
SHARED_LOCK = threading.Lock() 

def get_shared_orders():
    return SHARED_ORDERS


def get_lock():
    return SHARED_LOCK


def append_record(rec):
    """Append record inside manager process while holding the manager lock."""
    # e append ang record safely sa manager process gamit ang lock para synchronized ang access sa shared list
    SHARED_LOCK.acquire()
    try:
        SHARED_ORDERS.append(rec)
    finally:
        SHARED_LOCK.release()


OrderManager.register("get_shared_orders", callable=get_shared_orders, proxytype=ListProxy)
OrderManager.register("get_lock", callable=get_lock)
OrderManager.register("append_record", callable=append_record)


def generate_orders():
    return [
        {"order_id": 1, "item": "Ballpen"},
        {"order_id": 2, "item": "Yellow Pad"},
        {"order_id": 3, "item": "Pencil"},
        {"order_id": 4, "item": "Notebook"},
        {"order_id": 5, "item": "Correction Tape"},
        {"order_id": 6, "item": "Eraser"},
    ]


def assign_orders(orders, worker_count):
    assigns = [[] for _ in range(worker_count)]
    for i, o in enumerate(orders):
        assigns[i % worker_count].append(o)
    return assigns


def write_completed(shared_orders, manager_conn, order, rank, use_lock):
    rec = {"order_id": order["order_id"], "item": order["item"], "handled_by": rank}
    if use_lock:
        # ang synchronized write, e call ang manager-side append_record function nga mag handle sa pag append sa record sa shared list gamit ang lock para synchronized ang access sa shared list
        manager_conn.append_record(rec)
    else:
        # ang unsynchronized write, direct append ni siya sa shared list proxy without locking
        shared_orders.append(rec)


def main():
    from mpi4py import MPI

    # command-line arguments
    parser = argparse.ArgumentParser(description="Master-worker MPI demo")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--sync", action="store_true", help="use lock for shared writes")
    group.add_argument("--no-sync", action="store_true", help="no lock (show races)")
    args = parser.parse_args()

    # kani siya kay mag decide kung gamiton ba ang manager lock para sa pag write sa shared list, kung --no-sync ang gi specify, dili siya mag gamit ug lock, kung --sync or default, mag gamit siya ug lock para synchronized ang access sa shared list
    use_lock = not args.no_sync

    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    if size < 2:
        if rank == 0:
            print("Need at least 2 processes (1 master + workers)")
        return

    if rank == 0:
        # master ni siya nga mag ug create ug orders, start manager server, and distribute work
        orders = generate_orders()
        assigns = assign_orders(orders, size - 1)

        # start manager server nga mag listen sa free port sa localhost, ug mag expose sa shared list ug lock proxies nga ma access sa worker processes
        manager = OrderManager(address=("127.0.0.1", 0), authkey=b"orders")
        manager.start()
        addr = manager.address

        print("[MASTER] Generated orders:")
        for o in orders:
            print(f"  {o['order_id']}: {o['item']}")
        print(f"[MASTER] Mode: {'SYNC' if use_lock else 'UNSYNC'}")

        # mag send ni siya ug assignments ug manager address sa matag worker process gamit ang MPI send nga mag contain sa orders nga e-process sa worker, address sa manager server para maka connect sila, ug info kung gamiton ba ang lock para synchronized writes
        for w in range(1, size):
            comm.send({"orders": assigns[w - 1], "addr": addr, "sync": use_lock}, dest=w, tag=1)

        # mag connect ni siya as client sa manager server para ma access ang shared list after mahuman ang workers sa ilang processing
        conn = OrderManager(address=addr, authkey=b"orders")
        conn.connect()
        shared = conn.get_shared_orders()

        comm.Barrier()  # wait for workers to finish
  
        print("\n[MASTER] Completed orders (from shared list):")
        for r in shared:
            print(f"  Order {r['order_id']} ({r['item']}) handled by worker {r['handled_by']}")

        manager.shutdown()
    else:
        # mao ni ang worker nga mag receive ug orders and manager info, then process
        payload = comm.recv(source=0, tag=1)
        my_orders = payload["orders"]
        addr = payload["addr"]
        use_lock = payload["sync"]

        # mag connect ni siya as client sa manager server para ma access ang shared list ug lock proxies nga gi expose sa manager, para magamit niya ni sila sa pag append sa completed orders after processing
        conn = OrderManager(address=addr, authkey=b"orders")
        conn.connect()
        shared = conn.get_shared_orders()
        lock = conn.get_lock()

        print(f"[WORKER {rank}] Assigned orders: {[o['order_id'] for o in my_orders]} {'[LOCKED]' if use_lock else '[NO LOCK]'}")

        for o in my_orders:
            time.sleep(1)
            print(f"[WORKER {rank}] Processed order {o['order_id']}: {o['item']}")
            write_completed(shared, conn, o, rank, use_lock)

        comm.Barrier()


if __name__ == "__main__":
    main()
    