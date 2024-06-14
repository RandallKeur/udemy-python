""" Day 9 of Coding Challenges for Silent Auction"""
import os

from src.constants.ascii_art import AUCTION, GAVEL


def collect_bid(bids):
    """Collect bids from all people"""
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: "))
    if bid in bids:
        bids[bid].append(name)
    else:
        bids[bid] = [name]

    return bids


def print_winner(highest_bidders: list[str], bids: dict[int, list[str]]):
    """Display the winner of the auction"""
    print(f"{GAVEL}"
          f"The winner is {highest_bidders[0]} with a bid of ${max(bids)}")


def print_tie(highest_bidders: list[str], bids: dict[int, list[str]]):
    """Display the tie of the auction"""
    last_bidder = highest_bidders[-1]
    second_last_bidder = highest_bidders[-2]
    result = ''
    for bidder in highest_bidders:
        if bidder == second_last_bidder:
            result += bidder + ', and '
        elif bidder == last_bidder:
            result += bidder
        else:
            result += bidder + ', '
    print(f"{GAVEL}"
          f"We have a tie between {result} with a bid of ${max(bids)}")


def determine_winner(bids):
    """Determine the winner of the auction"""
    print(bids)
    highest_bidders = bids[max(bids)]
    print(highest_bidders)
    if len(highest_bidders) == 1:
        print_winner(highest_bidders, bids)
    else:
        print_tie(highest_bidders, bids)


def silent_auction():
    """Simulate a silent auction"""
    print(f"{AUCTION}"
          f"Welcome to the silent auction\n")
    bids = {}
    accepting_bids = True
    while accepting_bids:
        bids = collect_bid(bids)
        accepting_bids = input("Are there any other bidders? Type \"yes\" or \"no\": ") == 'yes'
        os.system('clear')

    determine_winner(bids)
