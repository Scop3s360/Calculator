import math

class operators:
    def add(self, input1, input2):
        return input1 + input2
    def minus(self, input1, input2):
        return input1 - input2
    def divide(self, input1, input2):
        return input1 / input2  
    def multiply(self, input1, input2): 
        return input1 * input2
    def squareroot(self, input1 ):
        return math.sqrt(input1)
    def square(self, input1):
        return input1 * input1
    def percen(self, input1, input2):
        return ((input1 / 100) * input2)

def main():

    input1 = None
    input2 = None
    selected_operator = None
    calc = operators()

    while True:
        print("=== Calculator Menu ===")
        print("1. Enter First Number")
        print("2. Enter Second Number")
        print("3. Select Operator")
        print("4. Show Current Values")
        print("5. Calculate")
        print("6. Exit")
        
        choice = input("Enter choice (1-6): ")

        if choice == '1':
            try:
                input1 = float(input("Enter first number: "))
                print(f"First number set to: {input1}")
            except ValueError:
                print("Please enter a valid number")

        elif choice == '2':
            try:
                input2 = float(input("Enter second number: "))
                print(f"Second number set to: {input2}")
            except ValueError:
                print("Please enter a valid number")

        elif choice == '3':
            print("Select Operator:")
            print("a. Addition")
            print("b. Subtraction")
            print("c. Multiplication")
            print("d. Division")
            print("e Square Root")
            print("f Percentage")
            print("g Square")
            op_choice = input("Enter choice (a-g): ")
            
            if op_choice == 'a':
                selected_operator = "add"
            elif op_choice == 'b':
                selected_operator = "minus"
            elif op_choice == 'c':
                selected_operator = "multiply"
            elif op_choice == 'd':
                selected_operator = "divide"
            elif op_choice == "e":
                selected_operator = "squareroot"
            elif op_choice == "f":
                selected_operator = "percen"
            elif op_choice == "g":
                selected_operator = "square"
            else:
                print("Invalid operator choice")
            
            if selected_operator:
                print(f"Operator set to: {selected_operator}")

        elif choice == '4':
            print("Current Values:")
            print(f"First Number: {input1}")
            print(f"Second Number: {input2}")
            print(f"Operator: {selected_operator}")

        elif choice == '5':
            if selected_operator is None:
                print("Please select an operator first")
            elif input1 is None:
                print("Please enter the first number")
            elif selected_operator in ["squareroot", "square"]:
                if selected_operator == "squareroot":
                    result = calc.squareroot(input1)
                else:
                    result = calc.square(input1)
                print(f"\nResult: {result}")
            elif input2 is None:
                print("Please enter the second number")
            else:
                if selected_operator == "divide" and input2 == 0:
                    print("Error: Cannot divide by zero!")
                else:
                    if selected_operator == "add":
                        result = calc.add(input1, input2)
                    elif selected_operator == "minus":
                        result = calc.minus(input1, input2)
                    elif selected_operator == "multiply":
                        result = calc.multiply(input1, input2)
                    elif selected_operator == "divide":
                        result = calc.divide(input1, input2)
                    elif selected_operator == "percen":
                        result = calc.percen(input1, input2)
                    
                    print(f"Result: {result}")

        elif choice == '6':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
