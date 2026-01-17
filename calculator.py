# Math functions

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

while True:
    print("\nChoose an operation.")
    print("1 - Add")
    print("2 - Subtract")

    choice = input("Enter choice: ")

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == "1":
        print("Result:", add(a, b))
    elif choice == "2":
        print("Result:", subtract(a, b))
    else:
        print("Invalid choice")

