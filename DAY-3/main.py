print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

crossroad = input('You\'re at a cross road. Where do you want to go? Type "left" or "right"\n').lower()

if crossroad == "left":
    lake = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
    if lake == "wait":
        house = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n').lower()
        if house == "red":
            print("It's a room full of fire. Game Over.")
        elif house == "blue":
            print("You enter a room of beasts. Game Over.")
        elif house == "yellow":
            print("You found the treasure! You Win!")
        else: 
            print("Invalid selection try again")
    elif lake == "swim":
        print("You get attacked by an angry trout. Game Over.")
    else:
        print("Invalid selection try again")
elif crossroad == "right":
    print("You fell into a hole. Game Over")
else:
    print("Invalid selection try again")