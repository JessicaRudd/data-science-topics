# Random module

import random

# # Random integer between 1 and 10
# random_integer = random.randint(1, 10)
# print(random_integer)

# # Random floating point number between [0, 1), not inclusive
# random_float = random.random()

# # Expand range
# random_float * 5
# # 0.0000... -> 4.9999....
# print(random_float)

# love_score = random.randint(1,100)
# print(f"Your love score is {love_score}")

# # Heads or Tails
# random_number = random.randint(0,1)

# if random_number == 1:
#     print("Heads")
# else:
#     print("Tails")

# Python Lists

# states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

## Change list item
# states_of_america[1] = "Pencilvania"

## Add item to list
# states_of_america.append("Puerto Rico")

## Extend list with additional list
# states_of_america.extend(["Puerto Rico","Guam"])
# print(states_of_america)

## Banker roulette
## Split string method
# test_seed = int(input("Create a seed number: "))
# random.seed(test_seed)

# Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")

# #Write your code below this line 👇
# #Get number of items in list
# num_items = len(names)
# random_name = names[random.randint(0,num_items-1)]

## Can also use random choice
# random_name = random.choice(names)
# print(f"{random_name} is going to buy the meal today!")

## Dirty dozen
## Nested lists
# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries",
# "Pears", "Tomatoes", "Celery", "Potatoes"]

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

# dirty_dozen =[fruits, vegetables]
# print(dirty_dozen)

## Treasure Map
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

horizontal = int(position[0]) - 1
vertical = int(position[1]) - 1

map[vertical][horizontal] = "X"

print(f"{row1}\n{row2}\n{row3}")