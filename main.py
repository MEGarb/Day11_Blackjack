import random
import os
from art import logo


def new_game(p_hand, p_score, d_hand, d_score, card):
    p_hand = []
    p_score = 0
    d_hand = []
    d_score = 0
    card = False
    os.system('cls')
    print(logo)

    return p_hand, p_score, d_hand, d_score, card


def deal_cards(hand, count):
    for _ in range(0, count):
        hand.append(random.choice(cards))
    return hand


def count_score(hand):
    score = 0
    for card in hand:
        score += card
    num_aces = hand.count(11)
    while num_aces > 0 and score > 21:
        num_aces -= 1
        score -= 10

    return score


def ask_another(score):
    if score > 21:
        return False

    if input("Would you like another card? 'y' or 'n'  ").lower() == 'y':
        return True
    else:
        return False


def dealer_play(hand):
    score = count_score(hand)

    while score < 17:
        deal_cards(hand, 1)
        score = count_score(hand)

    return hand, score


def who_wins(p_score, d_score):
    if p_score > 21 > d_score:
        print("Player busts!")
        print(f"Dealer wins with a score of {d_score} and you have {p_score}.\n")
    elif p_score < 21 < d_score:
        print("Dealer busts!")
        print(f"Player wins with a score of {p_score} and dealer has {d_score}.\n")
    elif p_score > d_score:
        print(f"Player wins with a score of {p_score} and dealer has {d_score}.\n")
    elif p_score < d_score:
        print(f"Dealer wins with a score of {d_score} and you have {p_score}.\n")
    elif p_score == d_score:
        print("Its a draw.")
        print(f"Player has a score of {p_score} and dealer has {d_score}.\n")
    else:
        print("This should not happen")
        print(f"player {p_score}   dealer {d_score}")


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
dealer_hand = []
player_hand = []
dealer_score = 0
player_score = 0
another_card = False
play_again = True
while play_again:
    player_hand, player_score, dealer_hand, dealer_score, another_card = new_game(player_hand, player_score, dealer_hand, dealer_score, another_card)
    player_hand = deal_cards(player_hand, 2)
    dealer_hand = deal_cards(dealer_hand, 2)
    player_score = count_score(player_hand)
    dealer_score = dealer_hand[0]
    print(f"Your hand is {player_hand} and your score is {player_score}.")
    print(f"The dealer is showing a {dealer_hand[0]}\n")
    another_card = ask_another(player_score)

    while another_card:
        player_hand = deal_cards(player_hand, 1)
        player_score = count_score(player_hand)
        print(f"Your hand is {player_hand} and your score is {player_score}.")
        print(f"The dealer is showing a {dealer_hand[0]}\n")
        another_card = ask_another(player_score)

    dealer_hand, dealer_score = dealer_play(dealer_hand)

    print(f"Your hand is {player_hand} and your score is {player_score}.")
    print(f"The dealer is showing a {dealer_hand} and has {dealer_score}\n")

    who_wins(player_score, dealer_score)

    if input("Do you want to play again? 'y' or 'n'  ").lower() == 'n':
        play_again = False

    print("\n")
