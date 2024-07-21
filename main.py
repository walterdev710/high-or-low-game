import art
from data import data
import random
from replit import clear

def format_text(account):
    account_name = account["name"]
    account_disc = account["description"]
    account_country = account["country"]
    return f"{account_name} a {account_disc}, from {account_country}"

def check_answer(guess, a_follower, b_follower):
    """ Take the user guess and follower counts and returns if they got it right """
    if a_follower > b_follower:
        if guess == "a":
            return True
        else:
            return False
    else:
        return guess == "b"


print(art.logo)
score =0

account_b = random.choice(data)

game_should_continue = True

while game_should_continue:
    # Generating random account from data

    account_a = account_b
    account_b = random.choice(data)


    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_text(account_a)}")
    print(art.vs)
    print(f"Against B: {format_text(account_b)}")

    # Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower() 

    # Check if user is correct
    a_follow_account = account_a["follower_count"]
    b_follow_account = account_b["follower_count"]

    is_correct = check_answer(guess, a_follow_account,b_follow_account)

    # Clear the screen between the rounds
    clear()
    print(art.logo)

    if is_correct:
        score += 1
        print(f"You're right! Current score is {score}")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong! Final score is {score}")