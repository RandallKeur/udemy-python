"""Day 10 of Coding Challenges for Calculator"""


from src.ascii_art.art import CALCULATOR


def calculator():
    print(f"{CALCULATOR}")
    number_1 = input("What\'s the first number?: ")
    print(f"+\n-\n*\n/\n")

    ##TODO loop here
    operation = input("Pick an operation: ")
    match operation:
        case '+':
            ## add
        case '-':
            subtract(number_1, number_2)
        case '*':
            multiply(number_1, number_2)
        case '/':
            divide(number_1, number_2)
        case _:
            print("Operation not valid")
            valid_op = False
