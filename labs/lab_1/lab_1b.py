"""
lab_1b.py

This is a script that implements a simple calculator. It takes two numbers and an operation,
then performs the operation and returns the result. 

The script asks the user to input the numbers and the operation to be performed,
and prints the result to the terminal window.

"""

def simple_calculator(operation: str, num1: float, num2: float) -> float:
    """
    Function that takes in two numbers and an operation (add, subtract, multiply, divide),
    then performs the operation on the two numbers and returns the result.

    Args:
        operation (str): The operation to perform ("add", "subtract", "multiply", "divide").
        num1 (float): The first number.
        num2 (float): The second number.

    Returns:
        float: The result of the operation.
    """

    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 != 0:
            return num1 / num2
        else:
            print("Cannot divide by zero. Try a different operation or numbers.")
            run_calculator()
    else:
        print("Invalid operation. Please choose from 'add', 'subtract', 'multiply', or 'divide'.")
        run_calculator()  # Prompt the user again for valid input


def run_calculator():
    # Ask the user for sample input    
    num1_string = input("Enter the first number: ")
    num2_string = input("Enter the second number: ")

    try:
        num1 = float(num1_string)
        num2 = float(num2_string)
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        run_calculator()  # Prompt the user again for valid input
    
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

    # Perform the calculation and display the result
    result = simple_calculator(operation, num1, num2)
    print(f"The result of {operation}ing {num1} and {num2} is: {result}")

def main():
    print(f"===== Simple Calculator =====")
    run_calculator()

    


if __name__ == "__main__":
    main()
