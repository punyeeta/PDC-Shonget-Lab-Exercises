import os
import pickle
import sys
import heapq
from concurrent.futures import ProcessPoolExecutor


DATASET_DIR = os.path.join(os.path.dirname(__file__), "datasets")
DATASETS = ["small_random.pkl", "medium_random.pkl", "large_random.pkl", "small_sorted.pkl", "medium_sorted.pkl", "large_sorted.pkl"]


# Local sort used per chunk.
def quicksort(data):
	if len(data) <= 1:
		return data
	pivot = data[len(data) // 2]
	left = [x for x in data if x < pivot]
	middle = [x for x in data if x == pivot]
	right = [x for x in data if x > pivot]
	return quicksort(left) + middle + quicksort(right)


def parallel_quicksort(data):
	if len(data) <= 1:
		return data
	# Instruction: divide data into 4 chunks.
	chunk_size = max(1, len(data) // 4)
	chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]
	# Instruction: sort chunks in separate processes.
	with ProcessPoolExecutor(max_workers=4) as ex:
		sorted_chunks = list(ex.map(quicksort, chunks))
	# Instruction: merge chunks into one globally sorted list.
	return list(heapq.merge(*sorted_chunks))


def load_dataset(filename):
	with open(os.path.join(DATASET_DIR, filename), "rb") as f:
		return pickle.load(f)


def choose_dataset():
	print("Choose a dataset:")
	for i, name in enumerate(DATASETS, start=1):
		print(f"{i}. {name}")
	print("Press Enter for default: small_random.pkl")
	choice = input("Enter choice (1-6): ").strip()
	if choice.isdigit():
		index = int(choice) - 1
		if 0 <= index < len(DATASETS):
			return DATASETS[index]
	return "small_random.pkl"


def parse_dataset_argument(args):
	if not args:
		return None
	arg = args[0].strip()
	if arg.isdigit():
		index = int(arg) - 1
		if 0 <= index < len(DATASETS):
			return DATASETS[index]
	if arg in DATASETS:
		return arg
	return None


def run_parallel_sort(filename="small_random.pkl"):
	data = load_dataset(filename)
	sorted_data = parallel_quicksort(data)
	print(f"Dataset: {filename}")
	print(f"Elements: {len(data)}")
	print(f"First 5: {sorted_data[:5]}")
	print(f"Last 5:  {sorted_data[-5:]}")
	# Quick global correctness check.
	print(f"Sorted Correctly: {all(sorted_data[i] <= sorted_data[i + 1] for i in range(len(sorted_data) - 1))}")
	return sorted_data


if __name__ == "__main__":
	selected_dataset = parse_dataset_argument(sys.argv[1:])
	if selected_dataset is None:
		selected_dataset = choose_dataset()
	run_parallel_sort(selected_dataset)
