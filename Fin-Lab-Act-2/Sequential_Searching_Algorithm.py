import pickle

def linear_search(data, target):
    for i in range(len(data)): #magpadayon hantod sa end sa dataset para makita ang index sa target
        if data[i] == target: #if makita si target ug iyang corresponsind index
            return i
    return -1 #if wala makita si i

def choose_dataset():
    options = {
        "1": "small_random.pkl",
        "2": "medium_random.pkl",
        "3": "large_random.pkl",
        "4": "small_sorted.pkl",
        "5": "medium_sorted.pkl",
        "6": "large_sorted.pkl",
    }

    print("Choose a dataset:")
    print("1. small_random.pkl")
    print("2. medium_random.pkl")
    print("3. large_random.pkl")
    print("4. small_sorted.pkl")
    print("5. medium_sorted.pkl")
    print("6. large_sorted.pkl")
    print("Press Enter for default: small_random.pkl")

    choice = input("Enter choice (1-6): ").strip() 
    return options.get(choice, "small_random.pkl")


if __name__ == "__main__":
    filename = choose_dataset()

    with open(f"datasets/{filename}", "rb") as f: #ang {filename} mag depende sa pilion sa user
        data = pickle.load(f)

    target = 437287 #arbitrary - bisag unsa nga value nga naa or wala sa dataset nga i-search

    result = linear_search(data, target)
    if result != -1: #kay -1 man ang ma return kung dili makita si target
        print(f"Found {target} at index {result}")
    else:
        print(f"{target} not found")