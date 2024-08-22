# # * Let's try to make calculator together, all you need to do is repair the code or fill the missing!


# # TODO: I want num_1 and numb_2 variables to store int data type not string so fix this lines to match the needs!
num_1 = int(input("Enter you first nummber : "))  # ! => int()
# * int("10")


num_2 = int(input("Enter you second nummber : "))
operation = input("Enter the opration you want : ")

# # * Try to understand the arguments of each function carefully the add function have two arguments (num_1, num_2)


def add(first_number, second_number):
    if type(first_number) != type(1) and type(second_number) != type(1):
        print("Bro chill, we need numbers!")
    else:
        print(first_number + second_number)


def sub(first_number, second_number):
    if type(first_number) != type(1) and type(second_number) != type(1):
        print("Bro chill, we need numbers!")
    else:
        print(first_number - second_number)


def multiply(first_number, second_number):
    if type(first_number) != type(1) and type(second_number) != type(1):
        print("Bro chill, we need numbers!")
    else:
        print(first_number * second_number)


def divide(first_number, second_number):
    if type(first_number) != type(1) and type(second_number) != type(1):
        print("Bro chill, we need numbers!")
    else:
        print(first_number / second_number)

# # TODO: Continue making functions for each operation until you done 4 currect (working!) functions!


def calculator(first_number, second_number, operation):
    # # TODO: Fix the condition underneath!
    if operation == "+":
        add(first_number, second_number)
    if operation == "-":
        # # * uncomment the function below, when you done making the function first!
        sub(num_1, num_2)
    if operation == "*":
        multiply(first_number, second_number)
    if operation == "/":
        divide(first_number, second_number)
    else:
        print("Bro this is alien operator!")

    # TODO: Link each function with its currect condition in the calculator function (we already did add, and sub)!


calculator(num_1, num_2, operation)

# # ? You might use these links for help!
# # * https://www.w3schools.com/python/python_conditions.asp
# # * https://www.w3schools.com/python/python_functions.asp
# # * https://www.w3schools.com/python/ref_func_input.asp

# # ?  Instructions: 1 - First repair the first two variable to handle int (numbers)!
# # ?                       2 - Create the missing functions up to 4 operations (don't forget what is arguments)!
# # ?                       3 - Link the functions with there parent (calculator function) take carefull look into what conditions you need to get the user with the operation he/she want!


# # ! Solution is down but try your best befoe looking down!

# # * down
# # * down
# # * down
# # * down
# # * down
# # * down
# # * down
# # * down
# # * down
# # * down
# # * down
# # * down
# # * down
# # * down
# # * down
# # * down
# # * down
# # * down
# # * down
# # * down
# # * down
# # * down
# # * down
# # * down
# # * down
# # * down
# # * down
# # * down
# # * down
# # * down
# # * down
# # * down
# # * down
# # * down
# # * down
# # * down
# # * down
# # * down
# # * down
# # * down
# # * down
# # * down
# # * down
# # * down
# # * down
# # * down
# # * down
# # * down
# # * down
# # * down
# # * down
# # * down
# # * down
# # * down
# # * down
# # * down
# # * down
# # * down
# # * down
# # * down
# # * down
# # * down
# # * down
# # * down
# # * down
# # * down
# # * down
# # * down
# # * down
# # * down
# # * down
# # * down

"""
num_1 = int(input("Enter first number : "))
num_2 = int(input("Enter second number : "))
operation = input("Enter the opration you want : ")


def add(num_1, num_2):
    print(num_1 + num_2)


def sub(num_1, num_2):
    print(num_1 - num_2)


def multiply(num_1, num_2):
    print(num_1 * num_2)


def divide(num_1, num_2):
    print(num_1 * num_2)


def calaulator(num_1, num_2, operation):
    if operation == "+":
        add(num_1, num_2)
    if operation == "-":
        sub(num_1, num_2)
    if operation == "*":
        multiply(num_1, num_2)
    if operation == "/":
        divide(num_1, num_2)


calaulator(num_1, num_2, operation)
"""
