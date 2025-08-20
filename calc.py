class operators:
    def add(self, input1, input2):
       return input1 + input2
    def minus(self, input1,input2):
       return input1 - input2
    def divide (self, input1,input2):
       return input1 / input2  
    def multiply (self, input1,input2):
       return input1 * input2
    
def main():

  input1 = None
  input2 = None

  calc=operators()

print("Basic Calc")
print("----------")

while True:
      print("=== Calc Options ===")
      print("1. Enter First Veriable")
      print("2. Enter Second Veriable")
      print("3. Select Operator")
      print("4. Clarify Sum")
      print("5. Calculate")
      print("6. Exit")

      choice = input("Enter your choice 1-6")

      if choice == '1':
        input1 = float(input("Enter your first number:"))

      elif choice == '2':
        input2 = float(input("Enter your first number:"))

      elif choice == '3':
          print("Addition (3a), Subtraction(3b), Multiplication(3c) or Divide(3d)")
          operator_choice = input("Enter your choice (3a/3b/3c/3d): ")
          
          if operator_choice == '3a':
              selected_operator = "add"
          elif operator_choice == '3b':
              selected_operator = "minus"
          elif operator_choice == '3c':
              selected_operator = "multiply"
          elif operator_choice == '3d':
              selected_operator = "divide"
          else:
              print("Invalid operator choice")
        
      elif choice == '4':
          if input1 is None or input2 is None or selected_operator is None:
              print("Please enter all numbers and select an operator first")
          else:
              operator_symbol = {
                  "add": "+",
                  "minus": "-",
                  "multiply": "*",
                  "divide": "/"
              }
              print(f"Your calculation will be: {input1} {operator_symbol[selected_operator]} {input2}")
        
      elif choice == 5:
            if input1 is None or input2 is None or selected_operator is None:
                print("Please enter all numbers and select an operator first")
            else:
                return input1 selected_operator input2
      
        if __name__== "__main__":
           main ()
