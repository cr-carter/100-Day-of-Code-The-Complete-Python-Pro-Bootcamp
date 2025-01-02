#The purpose of this program is gain more experience with defining functions, recursive functions,
#and utilizing dictionaries and lists to pass parameters to functions. As with previous programs,
#input validation was performed

#Function that will prompt user to enter a number based on user sequence (first, next, etc)
#Will validate input to check for whole number.
def get_number(sequence):
    not_number = True
    while not_number:
        number = input(f"What is the {sequence} number?: ")
        try:
            number = float(number)
            not_number = False
        except:
            print("Please type a number.")
    return number

#Function that will prompt user to choose an operation.
#Will validate to ensure that user inputs "+", "-", "*", or "/"
def get_operation():
    operator = ""
    while operator not in ["+", "-", "*", "/"]:
        operator = input("Pick an operation (+, -, *, /): ")
    return operator

#Functions that will add, subtract, multiply, or divide two numbers
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

#Dictionary that matches a key (math symbol in form of string)
#to a value (one of the previously defined functions)
operations = {"+": add,
              "-": subtract,
              "*": multiply,
              "/": divide,
              }
#Define a function that will act as a calculator.
def calculator():
    #Beginning of program, prompt user for first number
    first_number = get_number("first")

    #Enter a while loop that asks user for next number.
    #Allow user to continue performing operations based
    #upon value returned for each sequential operation
    continue_operations = True
    while continue_operations:
        #Prompt user for what type of operation they want to perform.
        operation_symbol = get_operation()
        #Prompt user for second/next number to perform calculation with.
        next_number = get_number("next")
        #Perform calculation, using dictionary to pass the two numbers to the appropriate operation function.
        calculation = operations[operation_symbol](first_number, next_number)
        #Show user the equation and solution.
        print(f"{first_number} {operation_symbol} {next_number} = {calculation}")
        
        #While loop to ask user if they want to perform another calculation using solution of previous calculation.
        #Also offer user ability to start a calculation with two new numbers, or to quit program.
        more_operations = ""
        while more_operations not in ["y", "n", "q"]:
            more_operations = input(f"Type 'y' to continue calculating with {calculation}, type 'n' to start new calculation, or type 'q' to quit. (y/n/q): ")

        if more_operations == "y":
            first_number = calculation
        elif more_operations == "n":
            calculator()
            continue_operations = False
        else:
            continue_operations = False

#Run the calculator program
calculator()
