import sys
from app.calculator import Calculator

def main():
    print("--- Interactive Calculator ---")
    print("Commands: add, sub, mul, div")
    print("Type 'exit' to close the program.")

    while True:
        user_input = input(">>> ").strip().lower()

        if user_input == "exit":
            print("Goodbye!")
            break

        parts = user_input.split()
        if len(parts) != 3:
            print("Invalid format. Use: <operation> <number1> <number2>")
            print("Example: add 5 10")
            continue

        operation, n1, n2 = parts

        try:
            num1 = float(n1)
            num2 = float(n2)

            if operation == 'add':
                print(f"Result: {Calculator.add(num1, num2)}")
            elif operation == 'sub':
                print(f"Result: {Calculator.subtract(num1, num2)}")
            elif operation == 'mul':
                print(f"Result: {Calculator.multiply(num1, num2)}")
            elif operation == 'div':
                print(f"Result: {Calculator.divide(num1, num2)}")
            else:
                print(f"Unknown operation '{operation}'. Use add, sub, mul, or div.")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()  # pragma: no cover