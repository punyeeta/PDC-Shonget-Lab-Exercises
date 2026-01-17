# Math functions

def add(a, b):
    return a + b


while True:
    print("\nChoose an operation.")
    print("1 - Add")

    choice = input("Enter choice: ")

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == "1":
        print("Result:", add(a, b))
    else:
        print("Invalid choice")