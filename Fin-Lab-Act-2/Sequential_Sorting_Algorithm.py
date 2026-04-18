import os
import pickle
import sys


DATASET_DIR = os.path.join(os.path.dirname(__file__), "datasets")
DATASETS = [
	"small_random.pkl",
	"medium_random.pkl",
	"large_random.pkl",
	"small_sorted.pkl",
	"medium_sorted.pkl",
	"large_sorted.pkl",
]


# Gigamitan ug quicksort algorithm para ma sort ang data nga gi load gikan sa dataset file and the best daw iyan kay O(n log n) ang average time complexity
def quicksort(data):
	if len(data) <= 1:
		return data

	# Gi split ang data into three parts: left (less than pivot), middle (equal to pivot), and right (greater than pivot)
	pivot = data[len(data) // 2]
	left = [x for x in data if x < pivot]
	middle = [x for x in data if x == pivot]
	right = [x for x in data if x > pivot]
	return quicksort(left) + middle + quicksort(right)


# Ipakita ang first 5 ug last 5 elements sa sorted data, ug i-verify kung sorted ba siya
def validate_first_last_five(sorted_data):
	first_five = sorted_data[:5]
	last_five = sorted_data[-5:]
	is_sorted = all(sorted_data[i] <= sorted_data[i + 1] for i in range(len(sorted_data) - 1))

	print(f"First 5: {first_five}")
	print(f"Last 5:  {last_five}")
	print(f"Sorted Correctly: {is_sorted}")


# E-load ang dataset gamit ang pickle module para ma read ang binary file nga gi save sa dataset_generator.py
def load_dataset(filename):
	path = os.path.join(DATASET_DIR, filename)
	with open(path, "rb") as file:
		return pickle.load(file)


# E-run ang quicksort algorithm sa usa ka selected dataset
def run_sequential_sort(filename="small_random.pkl"):
	data = load_dataset(filename)
	sorted_data = quicksort(data)

	print(f"Dataset: {filename}")
	print(f"Elements: {len(data)}")
	validate_first_last_five(sorted_data)

	return sorted_data


# Nag put mi ug interactive dataset picker
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

	# E-accept either ang dataset name or ang corresponding number sa dataset list
	arg = args[0].strip()
	if arg.isdigit():
		index = int(arg) - 1
		if 0 <= index < len(DATASETS):
			return DATASETS[index]
	if arg in DATASETS:
		return arg
	return None


if __name__ == "__main__":
	selected_dataset = parse_dataset_argument(sys.argv[1:])
	if selected_dataset is None:
		selected_dataset = choose_dataset()
	run_sequential_sort(selected_dataset)
