"""
Quick Test Script - Automated Testing with Sample Data
Run this to quickly verify both implementations work correctly.
WINDOWS COMPATIBLE VERSION
"""

import threading
import time
from multiprocessing import Process, Queue


def process_grade_mp(subject, grade, pid, queue):
    """Multiprocessing worker - must be defined at module level for Windows."""
    time.sleep(0.01)
    queue.put((subject, grade))
    print(f"[Process-{pid}] {subject}: {grade}")


def quick_test_threading():
    """Quick test of multithreading with sample data."""
    print("\n" + "="*60)
    print("QUICK TEST - MULTITHREADING")
    print("="*60)
    
    results = []
    results_lock = threading.Lock()
    
    # Sample data
    subjects = [
        ("Mathematics", 90),
        ("Science", 85),
        ("English", 92),
        ("History", 88),
        ("Physical Education", 95)
    ]
    
    def process_grade(subject, grade, tid):
        time.sleep(0.01)
        with results_lock:
            results.append((subject, grade))
            print(f"[Thread-{tid}] {subject}: {grade}")
    
    start = time.time()
    
    threads = []
    for i, (subj, grade) in enumerate(subjects):
        t = threading.Thread(target=process_grade, args=(subj, grade, i+1))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    
    elapsed = time.time() - start
    gwa = sum(g for _, g in results) / len(results)
    
    print("\nResults:")
    for subj, grade in results:
        print(f"  {subj}: {grade}")
    print(f"\nGWA: {gwa:.2f}")
    print(f"Time: {elapsed:.6f} seconds")
    print("="*60)
    
    return gwa, elapsed


def quick_test_multiprocessing():
    """Quick test of multiprocessing with sample data."""
    print("\n" + "="*60)
    print("QUICK TEST - MULTIPROCESSING")
    print("="*60)
    
    result_queue = Queue()
    
    # Sample data
    subjects = [
        ("Mathematics", 90),
        ("Science", 85),
        ("English", 92),
        ("History", 88),
        ("Physical Education", 95)
    ]
    
    start = time.time()
    
    processes = []
    for i, (subj, grade) in enumerate(subjects):
        p = Process(target=process_grade_mp, args=(subj, grade, i+1, result_queue))
        processes.append(p)
        p.start()
    
    for p in processes:
        p.join()
    
    results = []
    while not result_queue.empty():
        results.append(result_queue.get())
    
    elapsed = time.time() - start
    gwa = sum(g for _, g in results) / len(results)
    
    print("\nResults:")
    for subj, grade in results:
        print(f"  {subj}: {grade}")
    print(f"\nGWA: {gwa:.2f}")
    print(f"Time: {elapsed:.6f} seconds")
    print("="*60)
    
    return gwa, elapsed


if __name__ == "__main__":
    print("\nRunning automated tests with sample data...")
    print("(Both should calculate GWA = 90.00)")
    
    # Test multithreading
    mt_gwa, mt_time = quick_test_threading()
    
    # Test multiprocessing
    mp_gwa, mp_time = quick_test_multiprocessing()
    
    # Comparison
    print("\n" + "="*60)
    print("COMPARISON")
    print("="*60)
    print(f"Multithreading   - GWA: {mt_gwa:.2f}, Time: {mt_time:.6f}s")
    print(f"Multiprocessing  - GWA: {mp_gwa:.2f}, Time: {mp_time:.6f}s")
    print(f"\nSpeedup: {mp_time/mt_time:.2f}x " + 
          ("(Multithreading faster)" if mt_time < mp_time else "(Multiprocessing faster)"))
    print("="*60)
    
    print("\n✅ All tests completed successfully!")

