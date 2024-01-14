from art import logo, vs
from game_data import data
import random

print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

def format_data(account):
    account_name = account['name']
    account_descr = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_descr}, a {account_country}"

def check_answer(guess, a_follower_counts, b_follower_counts):
    if a_follower_counts > b_follower_counts:
        return guess == 'a'
    else:
        return guess == 'b'


while game_should_continue:
    account_a = random.choice(data)
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")


    guess = input("who has more followers? Type 'A' or 'B'").lower()

    a_follower_counts = account_a['follower_count']
    b_follower_counts = account_b['follower_count']

    is_correct = check_answer(guess, a_follower_counts, b_follower_counts)

    if is_correct:
        score += 1
        print(f"You're right!. your score is {score}")
    else:
        print(f"sorry, you are wrong. your final score is {score}")
        game_should_continue = False