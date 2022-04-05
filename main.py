import random
from art import logo
from replit import clear

# Return a random card from deck
def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10,10]
    card = random.choice(cards)
    return card


# calculate the score for cards
def calculate_score(cards):
    # If ace (11) in cards and score is over 21, remove 11 and add 1 to the list
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

# compare scores between user and computer
def compare(user_score, computer_score):

    if user_score > 21 and computer_score > 21:
        return "You went over. You lose!"

    elif user_score == computer_score:
        return "Draw!"

    elif computer_score == 21:
        return "Lose, opponent has Blackjack!"

    elif user_score == 21:
        return " Win with a Blackjack!"

    elif user_score > 21:
        return "You went over. You lose!"

    elif computer_score > 21:
        return "Opponent went over. You win!"

    elif user_score > computer_score:
        return "You win!"

    else:
        return "You lose!"

def play_game():

    print(logo)

    # Set up
    user_cards = []
    computer_cards = []
    game_over = False

    # Deal the user and computer 2 cards
    for n in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # Check if game is over with every new card drawn
    while not game_over:
        # If computer or user has a blackjack or if user's score is over 21, then game over
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        if user_score >=21 or computer_score == 21:
            game_over = True
        else:
            # Ask user if want to draw another card
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                game_over = True

    # Once user is done, computer should keep drawing cards as long as it has a score less than 17
    while computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score:{user_score}")
    print(f"Computer's final hand: {computer_cards}, final score:{computer_score}")
    print(compare(user_score, computer_score))

# Start the game
while input("Do you want to play a game of Blackjack: Type 'y' or 'n': ") == "y":
    clear()
    play_game()

















