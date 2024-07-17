""" Class including constant values"""

# CALCULATOR GAME
CALCULATOR_OPERATIONS = """
+
-
*
/
"""

# BLACKJACK GAME
BLACKJACK_CARDS = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
                   "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11}
HIT = "hit"
STAND = "stand"
BLACKJACK_21 = 21

# NUMBER GUESSING GAME
MIN = 1
MAX = 100
GUESSES = {"hard": 5, "medium": 6, "easy": 7}

# HIGHER LOWER GAME
CELEBRITIES = [
    {
        "name": "Cristiano Ronaldo",
        "follower_count": 215,
        "description": "Footballer",
        "country": "Portugal"
    },
    {
        "name": "Ariana Grande",
        "follower_count": 183,
        "description": "Musician and actress",
        "country": "United States"
    },
    {
        "name": "Dwayne Johnson",
        "follower_count": 181,
        "description": "Actor and professional wrestler",
        "country": "United States"
    },
    {
        "name": "Selena Gomez",
        "follower_count": 174,
        "description": "Musician and actress",
        "country": "United States"
    },
    {
        "name": "Kylie Jenner",
        "follower_count": 172,
        "description": "Reality TV personality and businesswoman and Self-Made Billionaire",
        "country": "United States"
    },
    {
        "name": "Kim Kardashian",
        "follower_count": 167,
        "description": "Reality TV personality and businesswoman",
        "country": "United States"
    },
    {
        "name": "Lionel Messi",
        "follower_count": 149,
        "description": "Footballer",
        "country": "Argentina"
    },
    {
        "name": "Beyoncé",
        "follower_count": 145,
        "description": "Musician",
        "country": "United States"
    },
    {
        "name": "Neymar",
        "follower_count": 138,
        "description": "Footballer",
        "country": "Brasil"
    },
    {
        "name": "National Geographic",
        "follower_count": 135,
        "description": "Magazine",
        "country": "United States"
    },
    {
        "name": "Justin Bieber",
        "follower_count": 133,
        "description": "Musician",
        "country": "Canada"
    },
    {
        "name": "Taylor Swift",
        "follower_count": 131,
        "description": "Musician",
        "country": "United States"
    },
    {
        "name": "Kendall Jenner",
        "follower_count": 127,
        "description": "Reality TV personality and Model",
        "country": "United States"
    },
    {
        "name": "Jennifer Lopez",
        "follower_count": 119,
        "description": "Musician and actress",
        "country": "United States"
    },
    {
        "name": "Nicki Minaj",
        "follower_count": 113,
        "description": "Musician",
        "country": "Trinidad and Tobago"
    },
    {
        "name": "Nike",
        "follower_count": 109,
        "description": "Sportswear multinational",
        "country": "United States"
    },
    {
        "name": "Khloé Kardashian",
        "follower_count": 108,
        "description": "Reality TV personality and businesswoman",
        "country": "United States"
    },
    {
        "name": "Miley Cyrus",
        "follower_count": 107,
        "description": "Musician and actress",
        "country": "United States"
    },
    {
        "name": "Katy Perry",
        "follower_count": 94,
        "description": "Musician",
        "country": "United States"
    },
    {
        "name": "Kourtney Kardashian",
        "follower_count": 90,
        "description": "Reality TV personality",
        "country": "United States"
    },
    {
        "name": "Kevin Hart",
        "follower_count": 89,
        "description": "Comedian and actor",
        "country": "United States"
    },
    {
        "name": "Ellen DeGeneres",
        "follower_count": 87,
        "description": "Comedian",
        "country": "United States"
    },
    {
        "name": "Real Madrid CF",
        "follower_count": 86,
        "description": "Football club",
        "country": "Spain"
    },
    {
        "name": "FC Barcelona",
        "follower_count": 85,
        "description": "Football club",
        "country": "Spain"
    },
    {
        "name": "Rihanna",
        "follower_count": 81,
        "description": "Musician and businesswoman",
        "country": "Barbados"
    },
    {
        "name": "Demi Lovato",
        "follower_count": 80,
        "description": "Musician and actress",
        "country": "United States"
    },
    {
        "name": "Victoria\'s Secret",
        "follower_count": 69,
        "description": "Lingerie brand",
        "country": "United States"
    },
    {
        "name": "Zendaya",
        "follower_count": 68,
        "description": "Actress and musician",
        "country": "United States"
    },
    {
        "name": "Shakira",
        "follower_count": 66,
        "description": "Musician",
        "country": "Colombia"
    },
    {
        "name": "Drake",
        "follower_count": 65,
        "description": "Musician",
        "country": "Canada"
    },
    {
        "name": "Chris Brown",
        "follower_count": 64,
        "description": "Musician",
        "country": "United States"
    },
    {
        "name": "LeBron James",
        "follower_count": 63,
        "description": "Basketball player",
        "country": "United States"
    },
    {
        "name": "Vin Diesel",
        "follower_count": 62,
        "description": "Actor",
        "country": "United States"
    },
    {
        "name": "Cardi B",
        "follower_count": 67,
        "description": "Musician",
        "country": "United States"
    },
    {
        "name": "David Beckham",
        "follower_count": 82,
        "description": "Footballer",
        "country": "United Kingdom"
    },
    {
        "name": "Billie Eilish",
        "follower_count": 61,
        "description": "Musician",
        "country": "United States"
    },
    {
        "name": "Justin Timberlake",
        "follower_count": 59,
        "description": "Musician and actor",
        "country": "United States"
    },
    {
        "name": "UEFA Champions League",
        "follower_count": 58,
        "description": "Club football competition",
        "country": "Europe"
    },
    {
        "name": "NASA",
        "follower_count": 56,
        "description": "Space agency",
        "country": "United States"
    },
    {
        "name": "Emma Watson",
        "follower_count": 56,
        "description": "Actress",
        "country": "United Kingdom"
    },
    {
        "name": "Shawn Mendes",
        "follower_count": 57,
        "description": "Musician",
        "country": "Canada"
    },
    {
        "name": "Virat Kohli",
        "follower_count": 55,
        "description": "Cricketer",
        "country": "India"
    },
    {
        "name": "Gigi Hadid",
        "follower_count": 54,
        "description": "Model",
        "country": "United States"
    },
    {
        "name": "Priyanka Chopra Jonas",
        "follower_count": 53,
        "description": "Actress and musician",
        "country": "India"
    },
    {
        "name": "9GAG",
        "follower_count": 52,
        "description": "Social media platform",
        "country": "China"
    },
    {
        "name": "Ronaldinho",
        "follower_count": 51,
        "description": "Footballer",
        "country": "Brasil"
    },
    {
        "name": "Maluma",
        "follower_count": 50,
        "description": "Musician",
        "country": "Colombia"
    },
    {
        "name": "Camila Cabello",
        "follower_count": 49,
        "description": "Musician",
        "country": "Cuba"
    },
    {
        "name": "NBA",
        "follower_count": 47,
        "description": "Club Basketball Competition",
        "country": "United States"
    }
]

# QUIZ GENERATOR
QUESTION_BANK = [
    {"question": "The capital of France is Paris.", "answer": "True"},
    {"question": "The Earth is flat.", "answer": "False"},
    {"question": "There are 365 days in a year.", "answer": "True"},
    {"question": "A leap year has 366 days.", "answer": "True"},
    {"question": "The chemical symbol for water is H2O.", "answer": "True"},
    {"question": "Humans have four hearts.", "answer": "False"},
    {"question": "The Great Wall of China is visible from space.", "answer": "False"},
    {"question": "Lightning never strikes the same place twice.", "answer": "False"},
    {"question": "The Sun is a star.", "answer": "True"},
    {"question": "Venus is the closest planet to the Sun.", "answer": "False"},
    {"question": "Humans breathe oxygen.", "answer": "True"},
    {"question": "An octopus has three hearts.", "answer": "True"},
    {"question": "Mount Everest is the tallest mountain on Earth.", "answer": "True"},
    {"question": "Penguins can fly.", "answer": "False"},
    {"question": "Bananas grow on trees.", "answer": "False"},
    {"question": "Sharks are mammals.", "answer": "False"},
    {"question": "The Amazon River is the longest river in the world.", "answer": "False"},
    {"question": "Sound travels faster than light.", "answer": "False"},
    {"question": "The human body has 206 bones.", "answer": "True"},
    {"question": "Jupiter is the largest planet in our solar system.", "answer": "True"},
    {"question": "Bats are blind.", "answer": "False"},
    {"question": "An ostrich\'s eye is bigger than its brain.", "answer": "True"},
    {"question": "Gold is heavier than silver.", "answer": "True"},
    {"question": "Water boils at 100 degrees Celsius.", "answer": "True"},
    {"question": "There are 12 months in a year.", "answer": "True"},
    {"question": "The capital of Japan is Beijing.", "answer": "False"},
    {"question": "Diamonds are made of carbon.", "answer": "True"},
    {"question": "The Pacific Ocean is the largest ocean on Earth.", "answer": "True"},
    {"question": "Giraffes have the same number of neck vertebrae as humans.", "answer": "True"},
    {"question": "There are 8 planets in our solar system.", "answer": "True"},
    {"question": "Humans have two lungs.", "answer": "True"},
    {"question": "The speed of light is faster than the speed of sound.", "answer": "True"},
    {"question": "A hexagon has five sides.", "answer": "False"},
    {"question": "A heptagon has seven sides.", "answer": "True"},
    {"question": "The Earth revolves around the Sun.", "answer": "True"},
    {"question": "Fish can drown.", "answer": "True"},
    {"question": "The Mona Lisa was painted by Vincent van Gogh.", "answer": "False"},
    {"question": "The square root of 9 is 3.", "answer": "True"},
    {"question": "Dogs are herbivores.", "answer": "False"},
    {"question": "An eagle is a bird of prey.", "answer": "True"},
    {"question": "Honey never spoils.", "answer": "True"},
    {"question": "The Eiffel Tower is in London.", "answer": "False"},
    {"question": "There are 50 states in the United States.", "answer": "True"},
    {"question": "Spiders are insects.", "answer": "False"},
    {"question": "The chemical symbol for gold is Au.", "answer": "True"},
    {"question": "The largest desert in the world is the Sahara.", "answer": "False"},
    {"question": "The capital of Australia is Sydney.", "answer": "False"},
    {"question": "The human heart has four chambers.", "answer": "True"},
    {"question": "Polar bears live in the Antarctic.", "answer": "False"},
    {"question": "A triangle has three sides.", "answer": "True"},
    {"question": "The capital of Italy is Rome.", "answer": "True"},
    {"question": "Lightning is hotter than the surface of the sun.", "answer": "True"},
    {"question": "A caterpillar turns into a butterfly.", "answer": "True"},
    {"question": "The atomic number of hydrogen is 1.", "answer": "True"},
    {"question": "Sharks have bones.", "answer": "False"},
    {"question": "The piano has 88 keys.", "answer": "True"},
    {"question": "Venus is the hottest planet in our solar system.", "answer": "True"},
    {"question": "The human eye can distinguish 10 million different colors.", "answer": "True"},
    {"question": "The fastest land animal is the cheetah.", "answer": "True"},
    {"question": "Albert Einstein developed the theory of general relativity.", "answer": "True"},
    {"question": "Mercury is the heaviest liquid.", "answer": "False"},
    {"question": "The capital of Canada is Ottawa.", "answer": "True"},
    {"question": "A group of lions is called a pride.", "answer": "True"},
    {"question": "The longest river in Africa is the Nile.", "answer": "True"},
    {"question": "Sharks lay eggs.", "answer": "True"},
    {"question": "The chemical symbol for iron is Fe.", "answer": "True"},
    {"question": "There are 5 continents in the world.", "answer": "False"},
    {"question": "Birds are reptiles.", "answer": "True"},
    {"question": "The capital of Egypt is Cairo.", "answer": "True"},
    {"question": "A person has 32 permanent teeth.", "answer": "True"},
    {"question": "An octopus has eight legs.", "answer": "False"},
    {"question": "An apple a day keeps the doctor away.", "answer": "False"},
    {"question": "The Atlantic Ocean is larger than the Indian Ocean.", "answer": "True"},
    {"question": "There are 7 colors in a rainbow.", "answer": "True"},
    {"question": "The sun rises in the west.", "answer": "False"},
    {"question": "A year on Mars is longer than a year on Earth.", "answer": "True"},
    {"question": "The smallest bone in the human body is in the ear.", "answer": "True"},
    {"question": "The Eiffel Tower was a gift from the United States to France.", "answer":
        "False"},
    {"question": "Butterflies taste with their feet.", "answer": "True"},
    {"question": "The largest planet in the solar system is Saturn.", "answer": "False"},
    {"question": "An adult human has 4 liters of blood.", "answer": "False"},
    {"question": "Cows can walk upstairs but not downstairs.", "answer": "True"},
    {"question": "Chocolate is toxic to dogs.", "answer": "True"},
    {"question": "Humans can breathe underwater without any equipment.", "answer": "False"},
    {"question": "A square has four equal sides.", "answer": "True"},
    {"question": "Bamboo is the fastest-growing plant.", "answer": "True"},
    {"question": "Light travels in a straight line.", "answer": "True"},
    {"question": "Humans share 50% of their DNA with bananas.", "answer": "True"},
    {"question": "Snakes have eyelids.", "answer": "False"},
    {"question": "A blue whale is the largest animal on Earth.", "answer": "True"},
    {"question": "The Statue of Liberty is in Washington, D.C.", "answer": "False"},
    {"question": "The capital of Germany is Berlin.", "answer": "True"},
    {"question": "The currency of Japan is the Yen.", "answer": "True"},
    {"question": "A bee dies after it stings.", "answer": "True"},
    {"question": "Humans have more than 5 senses.", "answer": "True"},
    {"question": "The capital of Spain is Madrid.", "answer": "True"},
    {"question": "A hexagon has six sides.", "answer": "True"}
]

# COFFEE MAKER
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
RESOURCES = {
    "water": 500,
    "milk": 350,
    "coffee": 132,
    "money": 0
}
UNITS_OF_MEASURE = {
    "water": "ml",
    "milk": "ml",
    "coffee": "ml",
    "money": "$"
}
COINS = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickels": 0.05,
    "pennies": 0.01
}

# TURTLE RACE
DEFAULT_TURTLE_DISTANCE = 50
TURTLE_COLORS = ["red", "orange", "yellow", "green", "blue", "purple", "black"]
TURTLE_SIZE = 40
RACE_DIMENSIONS = {
    "x": 500,
    "y": 400
}
MAX_VALUES = {
    "x": RACE_DIMENSIONS["x"] / 2 - TURTLE_SIZE / 2,
    "y": RACE_DIMENSIONS["y"] / 2 - 50
}
MIN_VALUES = {
    "x": - MAX_VALUES["x"],
    "y": - MAX_VALUES["y"]
}
Y_SPACING = (MAX_VALUES["y"] - MIN_VALUES["y"]) / (len(TURTLE_COLORS) - 1)

# SNAKE GAME
SNAKE_SPACING = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270
SNAKE_SCREEN_SIZE = 600
SNAKE_SCREEN = {
    "x": {
        "min": int(-SNAKE_SCREEN_SIZE / 2),
        "max": int(SNAKE_SCREEN_SIZE / 2)
    },
    "y": {
        "min": int(-SNAKE_SCREEN_SIZE / 2),
        "max": int(SNAKE_SCREEN_SIZE / 2)
    }
}
SNAKE_OFFSETS = {
    "food": 40,
    "scoreboard": 20
}
SNAKE_FOOD = {
    "x": {
        "min": int(SNAKE_SCREEN["x"]["min"] + SNAKE_OFFSETS["food"]),
        "max": int(SNAKE_SCREEN["x"]["max"] - SNAKE_OFFSETS["food"])
    },
    "y": {
        "min": int(SNAKE_SCREEN["y"]["min"] + SNAKE_OFFSETS["food"]),
        "max": int(SNAKE_SCREEN["x"]["max"] - SNAKE_OFFSETS["food"])
    }
}
GAME_SPEED = {
    "easy": 0.15,
    "medium": 0.10,
    "hard": 0.05
}

# PONG GAME
PONG_SCREEN_SIZE = {
    "x": 800,
    "y": 600
}
PONG_SCREEN = {
    "x": {
        "min": int(-PONG_SCREEN_SIZE["x"] / 2),
        "max": int(PONG_SCREEN_SIZE["x"] / 2)
    },
    "y": {
        "min": int(-PONG_SCREEN_SIZE["y"] / 2),
        "max": int(PONG_SCREEN_SIZE["y"] / 2)
    }
}
PONG_PADDLE_LOCATION = {
    "left": PONG_SCREEN["x"]["min"] + 50,
    "right": PONG_SCREEN["x"]["max"] - 50
}
PONG_OFFSETS = {
    "scoreboard": 50,
    "ball": 15,
    "paddle": 20
}
PONG_PADDLE_MOVEMENT = 20
PONG_BALL_MOVEMENT = 10

# TURTLE CROSSING
TURTLE_CROSSING_SCREEN_SIZE = 600
TURTLE_CROSSING_SCREEN = {
    "x": {
        "min": int(-TURTLE_CROSSING_SCREEN_SIZE / 2),
        "max": int(TURTLE_CROSSING_SCREEN_SIZE / 2)
    },
    "y": {
        "min": int(-TURTLE_CROSSING_SCREEN_SIZE / 2),
        "max": int(TURTLE_CROSSING_SCREEN_SIZE / 2)
    }
}
TURTLE_CROSSING_OFFSETS = {
    "player": 40,
    "scoreboard": 80
}
PLAYER_STARTING_Y_POSITION = TURTLE_CROSSING_SCREEN["y"]["min"] + TURTLE_CROSSING_OFFSETS["player"]
PLAYER_STARTING_POSITION = (0, PLAYER_STARTING_Y_POSITION)
PLAYER_MOVEMENT = 10
PLAYER_FINISH_LINE = TURTLE_CROSSING_SCREEN["y"]["max"] - TURTLE_CROSSING_OFFSETS["player"]
CAR_COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
CAR_MOVE_DISTANCE = 5
CAR_MOVE_INCREMENT = 10
SCOREBOARD_SETTINGS = {
    "locations": {
        "snake": (0, int(SNAKE_SCREEN["y"]["max"] - SNAKE_OFFSETS["scoreboard"])),
        "pong": (0, int(PONG_SCREEN["y"]["max"] - PONG_OFFSETS["scoreboard"])),
        "turtle_crossing": (int(TURTLE_CROSSING_SCREEN["x"]["min"] +
                                TURTLE_CROSSING_OFFSETS["scoreboard"]),
                            PLAYER_FINISH_LINE)
    },
    "game_over": "GAME OVER",
    "alignment": "center",
    "font": {
        "family": {
            "arial": "Arial",
            "courier": "Courier"
        },
        "weight": "normal",
        "size": {
            "small": 18,
            "large": 24,
            "x-large": 32,
            "xx-large": 48
        },
    }
}
OUTPUT_FILEPATH = "src/output_files/"
HIGH_SCORE_FILE = f"{OUTPUT_FILEPATH}high_score.txt"

# INVITATION BUILDER
CONSTANTS_FILEPATH = "src/constants/"
INVITATION_TEMPLATE = f"{CONSTANTS_FILEPATH}letter_template.txt"
GUESTS = f"{CONSTANTS_FILEPATH}invited_guests.txt"
INVITATION_OUTPUT_FILEPATH = OUTPUT_FILEPATH + "letters"

# STATES QUIZ
STATES_SCREEN_SIZE = {
    "x": 750,
    "y": 525
}
STATES_IMAGE = f"{CONSTANTS_FILEPATH}blank_states_img.gif"
STATES_FILE = f"{CONSTANTS_FILEPATH}50_states.csv"

# NATO CONVERTER
NATO_FILE = f"{CONSTANTS_FILEPATH}nato_phonetic_alphabet.csv"

# DISTANCE CONVERTER
MILES_TO_KM = 1.609

# POMODORO TIMER
POMODORO_CANVAS = {
    "width": 200,
    "height": 250
}
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
WORK = "WORK"
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
BREAK = "BREAK"
CYCLE = [
    {"text": WORK,
     "time": WORK_MIN},
    {"text": BREAK,
     "time": SHORT_BREAK_MIN},
    {"text": WORK,
     "time": WORK_MIN},
    {"text": BREAK,
     "time": SHORT_BREAK_MIN},
    {"text": WORK,
     "time": WORK_MIN},
    {"text": BREAK,
     "time": SHORT_BREAK_MIN},
    {"text": WORK,
     "time": WORK_MIN},
    {"text": BREAK,
     "time": LONG_BREAK_MIN}
]

# PASSWORD MANAGER
PASSWORD_CANVAS = {
    "width": 200,
    "height": 200
}
