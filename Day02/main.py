# bill splitter
print("Welcome to the bill splitter!")
total_bill = float(input("What was the total bill? $"))
tip = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
total_people = int(input("How many people to split the bill? "))

#Calculations
tip_amount = (tip * total_bill) / 100
total_bill = total_bill + tip_amount

splitted_bill = total_bill / total_people
print("Each person should pay: $",round(splitted_bill,2))
