import random

number = random.randint(1, 100)
easy_life = 10
hard_life = 5

print("Welcome to the Number guessing game!")
print("I am thinking of a number between 1 and 100.")
level = input("Chose a difficulty. Type 'easy' or 'hard': ")

def guess_loop(life, number):
    if life != 0:
        print(f"you have {life} attempts remining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == number:
            print("you got it. You Win!!!")
        elif guess > number:
            print("Too high")
            life -= 1
            guess_loop(life, number)
        elif guess < number:
            print("Too low")
            life -= 1
            guess_loop(life, number)
    else:
        print("you have run out of guess")
        print(f"the number you were looking for is {number}")

if level == "easy":
    guess_loop(easy_life, number)
elif level == "hard":
    guess_loop(hard_life, number)
else:
    print("Invalid selection. Try again")

