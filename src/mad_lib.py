"""MAD LIB game"""
from src.constants.values import PIZZA_DICTIONARY, PIZZA_STORY


def capture_input(key: str) -> str:
    value = ''
    while value == '':
        value = input(f'Enter value for {key}: ').strip()
        print(value)
    return value


def pizza_mad_lib():
    story = PIZZA_STORY
    dictionary = PIZZA_DICTIONARY
    for key in dictionary.keys():
        dictionary[key] = capture_input(key)
        story = story.replace(key, dictionary[key])

    print(story)
