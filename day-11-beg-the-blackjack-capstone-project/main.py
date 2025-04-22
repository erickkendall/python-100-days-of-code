# Day 11 - The Blackjack Capstone Project
# 100 Days of Code - Python Pro Bootcamp

from random import randint

# Constants
CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
BLACK_JACK = 21
DEALER_MINIMUM = 17


def deal_card():
    """Return a random card from the deck."""
    return CARDS[randint(0, len(CARDS) - 1)]


def hit_me(hand, is_dealer=False):
    """Add a card to the hand and evaluate the result."""
    hand.append(deal_card())
    score = sum(hand)
    
    if is_dealer:
        print(f"Dealer's cards: {hand}, current score: {score}")
    else:
        print(f"Your cards: {hand}, current score: {score}")
    
    hand_status = "continue"
    if score > BLACK_JACK:
        print("Bust!")
        hand_status = "bust"
    elif score == BLACK_JACK:
        print("Black Jack!")
        hand_status = "blackjack"
        
    return hand, hand_status


# Game setup
def play_blackjack():
    # Initialize hands
    player_hand = [deal_card(), deal_card()]
    dealer_hand = [deal_card(), deal_card()]

    # Calculate initial scores
    player_score = sum(player_hand)
    dealer_score = sum(dealer_hand)

    # Display initial game state
    print(f"Your cards: {player_hand}, current score: {player_score}")
    print(f"Dealer's first card: {dealer_hand[0]}")

    # Check for initial blackjack
    player_blackjack = (player_score == BLACK_JACK)
    dealer_blackjack = (dealer_score == BLACK_JACK)

    if player_blackjack and dealer_blackjack:
        print(f"Dealer's cards: {dealer_hand}, score: {dealer_score}")
        print("Both have Blackjack! Push :(")
        return
    elif player_blackjack:
        print("Blackjack! You win!")
        return
    elif dealer_blackjack:
        print(f"Dealer's cards: {dealer_hand}, score: {dealer_score}")
        print("Dealer has Blackjack. Dealer wins!")
        return

    # Player's turn
    player_busted = False
    
    while True:
        player_choice = input("Type 'y' to get another card, type 'n' to pass: ")
        if player_choice.lower() != 'y':
            break
        
        player_hand, player_status = hit_me(player_hand)
        if player_status != "continue":
            if player_status == "bust":
                player_busted = True
            break
    
    # Dealer's turn (only if player hasn't busted)
    if not player_busted:
        print(f"\nDealer's turn. Dealer's cards: {dealer_hand}, score: {dealer_score}")
        
        while sum(dealer_hand) < DEALER_MINIMUM:
            dealer_hand, dealer_status = hit_me(dealer_hand, is_dealer=True)
            if dealer_status != "continue":
                break
        
        # Compare final hands
        final_player_score = sum(player_hand)
        final_dealer_score = sum(dealer_hand)
        
        print(f"\nFinal scores - You: {final_player_score}, Dealer: {final_dealer_score}")
        
        if final_dealer_score > BLACK_JACK:
            print("Dealer busted! You win!")
        elif final_player_score > final_dealer_score:
            print("You win!")
        elif final_player_score < final_dealer_score:
            print("Dealer wins!")
        else:
            print("It's a tie! Push :(")
    else:
        print("You busted! Dealer wins.")


# Start the game
play_blackjack()
