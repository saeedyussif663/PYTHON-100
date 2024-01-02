print("Welcome to the tip calculator.")
total_bill = float(input("what was the total bill? $"))
tip = int(input("what percentage tip would you like to give? 10, 12, 15?"))
number_of_people = int(input("how many people to split the bill?"))

bill_plus_tip = (total_bill * (tip / 100)) + total_bill
each_person = round(bill_plus_tip / number_of_people, 2)
each_person = "{:.2f}".format(each_person)

print(f"Each person should pay: ${each_person}")