"""Class including constant values"""

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
        "name": "Victoria's Secret",
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
SCOREBOARD_SETTINGS = {
    "location": (0, int(SNAKE_SCREEN["x"]["max"] - SNAKE_OFFSETS["scoreboard"])),
    "game_over": "GAME OVER",
    "alignment": "center",
    "font": {
        "family": "Arial",
        "weight": "normal",
        "size": {
            "small": 18,
            "large": 24
        },
    }
}
SNAKE_SPEED = {
    "easy": 0.15,
    "medium": 0.10,
    "hard": 0.05
}
