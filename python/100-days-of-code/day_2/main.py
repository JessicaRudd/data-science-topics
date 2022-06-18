# #Data Types

# # String
# print("Hello"[4])

# print("123" + "345")

# #Integer
# print(123 + 345)

# # Float
# print(3.14159)

# # Boolean
# True
# False

# num_char = len(input("What is your name?"))
# #print(type(num_char))
# # Cannot concatenate int and strings
# print("Your name has " + str(num_char) + " characters.")

# print(70 + float("100.5"))
# print("70" + "100")

# # BMI Calculator

# # 🚨 Don't change the code below 👇
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# bmi = (float(weight) / float(height) ** 2)
# print(round(bmi, 2))

# #Number manipulation
# score = 0

# score += 1
# print(score)

# # F-strings
# score = 0
# height = 1.8
# isWinning = True

# print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}")


# Life left
# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

years_left = 90 - int(age)
days_left = (years_left)*365
weeks_left = years_left * 52
months_left = years_left * 12

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")