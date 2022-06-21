# loops

# fruits = ["Apple", "Peach", "Pear"]

# for fruit in fruits:
#     print(fruit)


# #Write your code below this row 👇
# student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

# max_score = 0
# for score in student_scores:
#     if score > max_score:
#         max_score = score

# print(f"The highest score in the class is: {max_score}")

# #For loop with range
# total = 0
# for number in range(1, 101):

#     total += number

# print(total)

# sum = 0

# for number in range(2,101, 2):

#     sum += number

# print(sum)

# ## Another way

# sum2 = 0
# for number in range(1,101):

#     if number % 2 == 0:
#         sum2 += number

# print(sum2)

## FizzBuzz game

for number in range(1,101):
    # Number divisible by 3 and 5
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")

    # Number divisible by 5
    elif number % 5 == 0:
        print("Buzz")

    # Number divisible by 3
    elif number % 3 == 0:
        print("Fizz")

    # Every other number in range just prints the number
    else:
        print(number)