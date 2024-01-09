from replit import clear
bids = {}

bidding_Done = False

while not bidding_Done:
    name = input("What is your name? ")
    price = int(input("What is your price? $ "))
    bids[name] = price

    should_continue = input("Are they any other user.Type 'yes' or 'no'")
    if should_continue == "no":
        should_continue = True
    elif should_continue == "yes":
        clear()

def find_higest_bidder():
    higgest_bid = 0
    winner = ""
    for key in bidding_Done:
        bid_amount = bidding_Done[key]
        if bid_amount > higgest_bid:
            higgest_bid = bid_amount
            winner = key
    print(f"The winner is {winner} with a bid of {higgest_bid}")
    