import math
class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            raise ValueError("Error: Division by zero is not allowed.")
        return x / y

    def exponentiate(self, x, y):
        return x ** y

    def square_root(self, x):
        if x < 0:
            raise ValueError("Error: Cannot take the square root of a negative number.")
        return math.sqrt(x)

    def calculate(self, operation, *args):
        operations = {
            '1': self.add,
            '2': self.subtract,
            '3': self.multiply,
            '4': self.divide,
            '5': self.exponentiate,
            '6': self.square_root
        }
        if operation in operations:
            return operations[operation](*args)
        else:
            raise ValueError("Invalid operation selected.")


def get_user_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a numeric value.")


def main():
    calculator = Calculator()
    print("Welcome to the Professional Calculator!")
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exponentiation (^)")
    print("6. Square Root (√)")

    history = []

    while True:
        choice = input("Enter choice (1/2/3/4/5/6) or 'q' to quit: ")

        if choice.lower() == 'q':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4', '5', '6']:
            if choice == '6':
                num1 = get_user_input("Enter a number: ")
                try:
                    result = calculator.calculate(choice, num1)
                    print(f"√{num1} = {result}")
                    history.append(f"√{num1} = {result}")
                except ValueError as e:
                    print(e)
            else:
                num1 = get_user_input("Enter first number: ")
                num2 = get_user_input("Enter second number: ")
                try:
                    result = calculator.calculate(choice, num1, num2)
                    operation_symbols = {
                        '1': '+',
                        '2': '-',
                        '3': '*',
                        '4': '/',
                        '5': '^'
                    }
                    print(f"{num1} {operation_symbols[choice]} {num2} = {result}")
                    history.append(f"{num1} {operation_symbols[choice]} {num2} = {result}")
                except ValueError as e:
                    print(e)
        else:
            print("Invalid choice! Please select a valid operation.")

        print("\nCalculation History:")
        for record in history:
            print(record)


if __name__ == "__main__":
    main()
