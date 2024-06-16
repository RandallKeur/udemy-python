"""Day 11 of Coding Challenges for Blackjack"""
import random

from src.constants.ascii_art import BLACKJACK
from src.constants.values import BLACKJACK_CARDS, HOLD, HIT, BLACKJACK_21


def deal_card() -> str:
    """Deal a random card for blackjack"""
    return random.choice(list(BLACKJACK_CARDS.keys()))


def deal_hand() -> list[str]:
    """Deal a hand for blackjack"""
    return [deal_card(), deal_card()]


def get_score(hand: list[str]):
    """Get current score for blackjack"""
    total = 0
    for card in hand:
        total += BLACKJACK_CARDS[card]
    if total > BLACKJACK_21 and 'A' in hand:
        hand.remove('A')
        hand.append('1')
        total -= 10

    return total


def determine_winner(player_hand: list[str], dealer_hand: list[str]):
    """Determine the winner of blackjack"""
    player_total = get_score(player_hand)
    dealer_total = get_score(dealer_hand)
    if player_total > BLACKJACK_21:
        print(f'Player bust, Dealer wins with {dealer_total}')
    elif dealer_total > BLACKJACK_21:
        print(f'Dealer bust, Player wins with {player_total}')
    elif player_total > dealer_total:
        print(f'Player wins with {player_total} and dealer with {dealer_total}')
    elif player_total < dealer_total:
        print(f'Dealer wins with {dealer_total} and player with {player_total}')
    else:
        print('Push!')


def dealer_hits(dealer_hand: list[str]) -> list[str]:
    """Blackjack dealer continues to take cards until at they are at 17"""
    while get_score(dealer_hand) < 17:
        new_card = deal_card()
        dealer_hand.append(new_card)
        print(f'Dealer deals himself {new_card}')
    return dealer_hand


def blackjack():
    """Blackjack dealer game"""
    print(BLACKJACK)
    player_hand = deal_hand()
    dealer_hand = deal_hand()
    print(f'Your cards: {player_hand}')
    print(f'Dealer\'s first card: {dealer_hand[0]}')
    bust = hold = False
    while not bust and not hold:
        hold = input(f'Type \'{HIT}\' to get another card, type \'{HOLD}\' to pass: ') == {HOLD}
        if not hold:
            new_card = deal_card()
            player_hand.append(new_card)
            print(f'Dealer deals you a \'{new_card}\', your hand is now {player_hand}')
            bust = get_score(player_hand) > BLACKJACK_21

    print(f'Dealer shows {dealer_hand[1]}')
    dealer_hand = dealer_hits(dealer_hand)

    determine_winner(player_hand, dealer_hand)
