# Distributed Order Processing Demo — Exact Outputs and Simple Explanation

## Unsynchronized run (exact output)

```text
[WORKER 2] Assigned orders: [2, 5] [NO LOCK]
[WORKER 2] Processed order 2: Mouse
[WORKER 2] Processed order 5: Headphones
[WORKER 3] Assigned orders: [3, 6] [NO LOCK]
[WORKER 3] Processed order 3: Keyboard
[WORKER 3] Processed order 6: USB Cable
[WORKER 1] Assigned orders: [1, 4] [NO LOCK]
[WORKER 1] Processed order 1: Laptop
[WORKER 1] Processed order 4: Monitor
[MASTER] Generated orders:
	1: Laptop
	2: Mouse
	3: Keyboard
	4: Monitor
	5: Headphones
	6: USB Cable
[MASTER] Mode: UNSYNC

[MASTER] Completed orders (from shared list):
	Order 2 (Mouse) handled by worker 2
	Order 1 (Laptop) handled by worker 1
	Order 3 (Keyboard) handled by worker 3
	Order 4 (Monitor) handled by worker 1
	Order 6 (USB Cable) handled by worker 3
	Order 5 (Headphones) handled by worker 2
```

## Synchronized run (exact output)

```text
[WORKER 3] Assigned orders: [3, 6] [LOCKED]
[WORKER 3] Processed order 3: Keyboard
[WORKER 3] Processed order 6: USB Cable
[WORKER 2] Assigned orders: [2, 5] [LOCKED]
[WORKER 2] Processed order 2: Mouse
[WORKER 2] Processed order 5: Headphones
[WORKER 1] Assigned orders: [1, 4] [LOCKED]
[WORKER 1] Processed order 1: Laptop
[WORKER 1] Processed order 4: Monitor
[MASTER] Generated orders:
	1: Laptop
	2: Mouse
	3: Keyboard
	4: Monitor
	5: Headphones
	6: USB Cable
[MASTER] Mode: SYNC

[MASTER] Completed orders (from shared list):
	Order 1 (Laptop) handled by worker 1
	Order 2 (Mouse) handled by worker 2
	Order 3 (Keyboard) handled by worker 3
	Order 4 (Monitor) handled by worker 1
	Order 5 (Headphones) handled by worker 2
	Order 6 (USB Cable) handled by worker 3
```

## Simple explanation (plain words)

- Unsynchronized run (what happened):
	- Workers wrote to the shared list at the same time without asking permission.
	- Because writes can overlap, the final order of completed records is not predictable.

- Synchronized run (what happened):
	- Workers used a lock so only one could write at a time.
	- This made the final recorded order stable and repeatable across runs.

Why this matters
- When many processes share the same data, uncoordinated writes can give different results each run.
- A simple lock makes writes happen one-by-one, avoiding those unpredictable results.

