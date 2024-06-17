"""Day 10 of Coding Challenges for Calculator"""

from src.constants.ascii_art import CALCULATOR
from src.constants.values import CALCULATOR_OPERATIONS


def collect_input():
    """Collect input number from the user"""
    return input('What\'s the next number?: ')


def get_operation(number_1: float) -> float:
    """Get calculator operation from input and return result"""
    valid_op = False
    while not valid_op:
        operation = input(f'{CALCULATOR_OPERATIONS}'
                          'Pick an operation: ')
        valid_op = True
        match operation:
            case '+':
                number_1 += float(collect_input())
            case '-':
                number_1 -= float(collect_input())
            case '*':
                number_1 *= float(collect_input())
            case '/':
                number_1 /= float(collect_input())
            case _:
                print('Operation not valid\n')
                valid_op = False
    return number_1


def calculator():
    """Calculator"""
    print(f'{CALCULATOR}')
    continue_with_result = False
    running = True
    result = 0
    while running:
        if not continue_with_result:
            number_1 = float(input('What\'s the first number?: '))
        else:
            number_1 = result

        result = get_operation(number_1)
        response = input(f'Type \'y\' to continue with {result}, or \'n\' to start a '
                         'new calculation, or \'STOP\' to end the program: ')
        match response:
            case 'y':
                continue_with_result = True
            case 'n':
                continue_with_result = False
            case 'STOP':
                running = False
