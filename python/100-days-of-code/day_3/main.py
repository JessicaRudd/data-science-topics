# print("Welcome to the rollercoaster!")
# # Note: 1 equal sign is an 'assignment', 2 equal signs is a T/F evaluation
# height = int(input("What is your height in in?\n"))

# if height > 48:
#     print("You can ride!")
# else:
#     print("Sorry! You're not tall enough to ride!")


# ## Even / odd
# # 🚨 Don't change the code below 👇
# number = int(input("Which number do you want to check? "))
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# remainder = number % 2

# if remainder == 0:
#     print("This is an even number.")
# else:
#     print("This is an odd number.")

# Nested if/else
print("Welcome to the rollercoaster!")
# # Note: 1 equal sign is an 'assignment', 2 equal signs is a T/F evaluation
height = int(input("What is your height in in?\n"))
bill = 0

if height > 48:
    print("You can ride!")
    age = int(input("What is your age?\n"))
    if age < 12:
        bill = 5
        print("Child tickets $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets $7.")
    
    elif age >= 45 and age <=55:
        print("Your ticket is free!")
        
    else:
        bill = 12
        print("Adult tickets $12.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        # Add $3 to their ticket
        bill+=3

    print(f"Your ticket costs ${bill}")

else:
    print("Sorry! You're not tall enough to ride!")

# # 🚨 Don't change the code below 👇
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# bmi = int(round((float(weight) / float(height) ** 2), 0))

# if bmi <= 18.5:
#     print(f"Your BMI is {bmi}, you are underweight.")
# elif bmi < 25:
#     print(f"Your BMI is {bmi}, you have a normal weight.")
# elif bmi < 30:
#     print(f"Your BMI is {bmi}, you are slightly overweight.")
# elif bmi < 35:
#     print(f"Your BMI is {bmi}, you are obese.")
# else:
#     print(f"Your BMI is {bmi}, you are clinically obese.")

# # 🚨 Don't change the code below 👇
# year = int(input("Which year do you want to check? "))
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇

# if year % 4 == 0:

#     if year % 100 == 0:

#         if year % 400 == 0:

#             print("Leap year.")
        
#         else:

#             print("Not leap year.")
        
#     else:

#         print("Leap year.")

# else:

#     print("Not leap year.")

