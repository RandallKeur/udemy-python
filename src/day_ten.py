"""Day 10 of Coding Challenges for Calculator"""


from src.ascii_art.art import CALCULATOR


def collect_input():
    return input("What\'s the next number?: ")


def calculator():
    print(f"{CALCULATOR}")
    number_1 = input("What\'s the first number?: ")
    print(f"+\n-\n*\n/\n")

    valid_op = False
    while not valid_op:
        operation = input("Pick an operation: ")
        valid_op = True
        match operation:
            case '+':
                number_1 += collect_input()
            case '-':
                number_1 -= collect_input()
            case '*':
                number_1 *= collect_input()
            case '/':
                number_1 /= collect_input()
            case _:
                print("Operation not valid\n")
                valid_op = False
