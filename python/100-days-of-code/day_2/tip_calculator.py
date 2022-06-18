print("Welcome to the tip calculator!\n")
bill = float(input("What was the total bill?\n"))
tip = int(input("What percentage tip would you like to give? [Popular tips = 10 / 12 / 15%]\n"))
bill_divide = int(input("How many people to split the bill?"))

# Ex. If the bill was $150.00, split between 5 people, with 12% tip:
# Each person should pay (150.00 / 5) * 1.12

total = round(bill * (1 + tip/100), 2)
share = round(total/bill_divide, 2)

print(f"Each person should pay ${share}, resulting in total of ${total}.")


