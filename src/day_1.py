""" Day 1 of Coding Challenges for generating a band name"""
RESPONSE = 'Your band name is'


def band_name_generator():
    """ Generate a band name"""
    print('Welcome to the Band Name Generator')
    city = input('What city did you grow up in?\n')
    pet_name = input('What is your pet\'s name?\n')
    print(f'{RESPONSE} {city} {pet_name}')
