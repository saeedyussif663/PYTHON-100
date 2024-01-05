import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

selected_password = []
shuffled_password = []

for i in range(0,nr_letters):
   selection = random.randint(0, len(letters) - 1)
   selected_password.append(letters[selection])

for i in range(0, nr_symbols):
   selection = random.randint(0, len(symbols) - 1)
   selected_password.append(symbols[selection])

for i in range(0, nr_numbers):
   selection = random.randint(0, len(numbers) - 1)
   selected_password.append(numbers[selection])

for i in range(0, len(selected_password)):
   selection = random.randint(0, len(selected_password) - 1)
   shuffled_password.append(selected_password[selection])

password = "".join(shuffled_password)
   
print(f"your magical password is {password}")