#The purpose of this project is to practice with the following concepts:
#Mathematical operations, data types, number manipulation, f-strings, and formating

#Welcome message
print("Welcome to the tip calculator!")

#Input total bill
bill = float(input("What was the total bill?\n"))

#Input tip percentage
tip = int(input("What percentage tip would you like to give? (10, 12, 15, 20)\n"))

#Input number of people splitting bill
people = int(input("How many people are splitting the bill?\n"))

#Calculate total bill with tip
bill_with_tip = bill * (1 + (tip/100))

#Calculate how much each person will pay
per_person = bill_with_tip / people

#Convert to proper format (:.2f means that it will produce a fixed-point number with 2 numbers after the .150)
per_person = '{:.2f}'.format(per_person)

#Print answer
print(f"Each person will pay ${per_person}")
