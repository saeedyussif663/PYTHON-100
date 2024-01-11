import random

user_cards = []
computer_cards = []
is_game_over = False

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 0:
        return 0
    if 11 in cards and sum(cards) == 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "draw"
    elif computer_score == 0:
        return "you lost, computer has a black jack"
    elif user_score == 0:
        return "you won, user has a black jack"
    elif user_score > 21:
        return "you went over, you lost"
    elif computer_score > 21:
        return "computer went over, you won"
    elif user_score > computer_score:
        return "you won"
    else:
        return "you lost"
    

for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(user_score, user_cards)
    print(computer_cards[0])


    if user_score == 0 or user_score > 21 or computer_score == 0:
        is_game_over = True
    else:
        user_should_deal = input("Type y to get another card. otherwise type n to pass ")
        if user_should_deal == "y":
            user_cards.append(deal_card())
        else:
            is_game_over = True

while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

compare(user_score, computer_score)