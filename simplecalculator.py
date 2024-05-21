def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero."
    
def main():
    while True:
        print("\nSimple Calculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Quit")

        choice = input("Choose an operation (1/2/3/4/5): ")

        if choice in ['1', '2', '3', '4']:
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numeric values.")
                continue

            if choice == '1':
                print(f"The result is: {add(a, b)}")
            elif choice == '2':
                print(f"The result is: {subtract(a, b)}")
            elif choice == '3':
                print(f"The reslut is: {multiply(a, b)}")
            elif choice == '4':
                result = divide(a, b)
                print(f"The result is: {result}")
        elif choice == '5':
            print("Exiting the calculator. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid operation.")

if __name__ == "__main__":
    main()