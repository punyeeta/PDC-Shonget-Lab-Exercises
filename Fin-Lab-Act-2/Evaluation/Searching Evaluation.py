import sys
import os
import pickle
import time

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from Sequential_Searching_Algorithm import linear_search
from Parallel_Searching_Algorithm import parallel_search

datasets = [
    "small_random.pkl",
    "medium_random.pkl",
    "large_random.pkl",
    "small_sorted.pkl",
    "medium_sorted.pkl",
    "large_sorted.pkl",
]

if __name__ == "__main__":
    for filename in datasets:
        with open(f"../datasets/{filename}", "rb") as f:
            data = pickle.load(f)

        target = 4665

        start = time.time()
        seq_result = linear_search(data, target)
        seq_time = time.time() - start

        start = time.time()
        par_result = parallel_search(data, target)
        par_time = time.time() - start

        seq_index = str(seq_result) if seq_result != -1 else "not found"
        par_index = str(par_result) if par_result != -1 else "not found"

        print(f"Dataset: {filename}")
        print(f"Target: {target}")
        print(f"Sequential - Index: {seq_index}, Time: {seq_time:.6f}s")
        print(f"Parallel   - Index: {par_index}, Time: {par_time:.6f}s")
        print()