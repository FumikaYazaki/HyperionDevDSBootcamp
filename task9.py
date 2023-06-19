#Ask users to choose an option from option 1 and 2
choice = input("Please choose an option number, either 1: enter two numbers and an operator, or 2: read all of the equations from a new txt file")

#For option 1
if choice == "1":
    # Ask users to input numbers and operation
    try:
        entered_num1 = int(input("Please enter first number"))
        entered_num2 = int(input("Please enter second number"))
        entered_operation = input("Please enter an operation 'e.g. +,-,x,/)'.")
    except Exception:
        print("That was not valid number or operation. Please try it again.")
    #Equations
    else:
        equation = f"{entered_num1} {entered_operation} {entered_num2}"
        if entered_operation == "+":
            answer = entered_num1 + entered_num2
        elif entered_operation == "-":
            answer = entered_num1 - entered_num2
        elif entered_operation == "*":
            answer = entered_num1 * entered_num2
        elif entered_operation == "/":
            if entered_num2 != 0:
                answer = entered_num1 / entered_num2
            else:
                print("Division by zero is not allowed. Please enter another number.")
                answer = None
        #In the case users input invalid operation
        else:
            print("That was not valid operation. Please try it again.")
            answer = None
        #Final result
        if answer is not None:
            print(f"Result is {answer}")

            #Ask the user to name the file to store the equation
            filename = input("Please enter a name of the text file")
            #Write the equation to a text file
            with open(filename, "a") as file:
                file.write(equation + "=" + str(answer)) 

#For option 2          
elif choice == "2":
    while True:
    #Ask users to input file name they want to read
        filename = input("Please enter the file name")
        try:
            with open(filename, "r") as file:
                equations = file.readlines()
        #Show users equations stored in the file
            for equation in equations:
                equation = equation.strip()
                print(f"Equation is {equation}")
        #In the case users input invalid file name
        except FileNotFoundError:
            print("The file does not exist. Enter the file name again.")
#In the case users input invalid option number
else:
    print("Invalid choice.")