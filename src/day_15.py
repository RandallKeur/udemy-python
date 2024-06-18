""" Day 15 of Coding Challenges for coffee machine"""
from src.constants.ascii_art import COFFEE
from src.constants.values import MENU, RESOURCES, COINS, UNITS_OF_MEASURE


def print_report(resources: dict[str, int]):
    """Print report for the Coffee Maker resources"""
    for key, value in resources.items():
        uom = UNITS_OF_MEASURE[key]
        print(f'{key}: {value} ({uom})')


def calculate_money(money: dict[str, int]) -> float:
    """Calculate the total money inserted into the Coffee Maker"""
    total = 0
    for coin, quantity in money.items():
        total += quantity * COINS[coin]
    return total


def collect_money() -> float:
    """Collect the money for the Coffee Maker"""
    print('Please insert coins.')
    money = {
        'quarters': int(input('How many quarters?: ')),
        'dimes': int(input('How many dimes?: ')),
        'nickels': int(input('How many nickels?: ')),
        'pennies': int(input('How many pennies?: '))
    }
    return calculate_money(money)


def get_ingredients(request: str) -> dict[str, int]:
    """Get the ingredients from the Coffee Maker"""
    return MENU[request]['ingredients'].items()


def has_enough_resources(request: str, resources: dict[str, int]) -> bool:
    """Check whether there are enough resources for the Coffee Maker"""
    ingredients = get_ingredients(request)
    for ingredient, quantity in ingredients:
        if quantity > resources.get(ingredient):
            print(f'Sorry, there is not enough {ingredient}')
            return False

    return True


def on_menu(request) -> bool:
    """Check whether the requested item is on the menu"""
    item = MENU.get(request)
    if item is None:
        print(f'Sorry, {request} is not in the menu.')
    return item is not None


def get_cost(request: str) -> float:
    """Get total cost of the requested item"""
    return MENU[request]['cost']


def process_order(request: str, money: float, resources: dict[str, int]) -> dict[str, int]:
    """Process the order for the requested item"""
    ingredients = get_ingredients(request)
    cost = get_cost(request)
    for ingredient, quantity in ingredients:
        resources[ingredient] -= quantity
    resources['money'] += MENU[request]['cost']
    print(f'Here is ${money - cost:.2f} in change.')
    print(f'Here is your {request} ☕️ Enjoy!')
    return resources


def has_enough_money(request: str, money: float) -> bool:
    """Check if the money inserted is enough for the requested item"""
    cost = get_cost(request)
    if money >= cost:
        return True
    print('Sorry, that\'s not enough money. Money refunded.')
    return False


def coffee_maker():
    """Make a coffee for a customer"""
    print(f'{COFFEE}')
    resources = RESOURCES
    stop = False
    while not stop:
        request = input('What would you like? (espresso/latte/cappuccino): ')
        match request:
            case 'report':
                print_report(resources)
            case 'off':
                break
        if on_menu(request):
            if has_enough_resources(request, resources):
                money = collect_money()
                if has_enough_money(request, money):
                    resources = process_order(request, money, resources)
