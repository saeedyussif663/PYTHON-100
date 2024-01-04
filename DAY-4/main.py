import random

print("welcome to the best rock, paper, scissors game you will ever come across")
choice = input("which do you choose? 1 for rock, 2 for paper, 3 for scissors ")
choice = int(choice)

computers_choice = random.randint(1,3)


if choice == 1:
    print(f"you chose rock")
elif choice == 2:
    print("you chose paper")
elif choice == 3:
    print("you chose scissors")

if choice == computers_choice:
    print("you both chose the same item. DRAW!!!")
elif choice == 1 and computers_choice == 2:
    print("computer chose paper. you LOST!!!")
elif choice == 2 and computers_choice == 3:
    print("computer chose scisors. you LOST!!!")
elif choice == 3 and computers_choice == 1:
    print("computer chose rock. you LOST!!!")
elif choice == 3 and computers_choice == 2:
    print("computer chose paper. you WON!!!")
elif choice == 2 and computers_choice == 1:
    print("computer chose rock, you WON!!!")
elif choice == 1 and computers_choice == 3:
    print("computer chose scissors, you WON!!!")
else:
    print("INVALID SELECTION")