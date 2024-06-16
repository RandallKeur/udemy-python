"""Day 11 of Coding Challenges for Blackjack"""
import random

from src.constants.ascii_art import BLACKJACK
from src.constants.values import BLACKJACK_CARDS


def deal_card() -> str:
    return random.choice(list(BLACKJACK_CARDS.keys()))


def deal_hand() -> list[str]:
    return [deal_card(), deal_card()]


def get_score(hand: list[str]):
    total = 0
    for card in hand:
        total += BLACKJACK_CARDS[card]
    return total


def determine_winner(player_hand: list[str], dealer_hand: list[str]):
    player_total = get_score(player_hand)
    dealer_total = get_score(dealer_hand)
    if player_total > 21:
        print(f'Player bust, Dealer wins with {dealer_total}')
    elif dealer_total > 21:
        print(f'Dealer bust, Player wins with {player_total}')
    elif player_total > dealer_total:
        print(f'Player wins with {player_total} and dealer with {dealer_total}')
    elif player_total < dealer_total:
        print(f'Dealer wins with {dealer_total} and player with {player_total}')
    else:
        print('Push!')


def blackjack():
    print(BLACKJACK)
    player_hand = deal_hand()
    dealer_hand = deal_hand()
    print(f'Your cards: {player_hand}')
    print(f'Dealer\'s first card: {dealer_hand[0]}')
    bust = hold = False
    while not bust and not hold:
        hold = input('Type \'y\' to get another card, type \'n\' to pass: ') == 'n'
        if not hold:
            new_card = deal_card()
            player_hand.append(new_card)
            print(f'Dealer deals you a \'{new_card}\', your hand is now {player_hand}')
            bust = get_score(player_hand) > 21

    while get_score(dealer_hand) < 17:
        dealer_hand.append(deal_card())

    determine_winner(player_hand, dealer_hand)
