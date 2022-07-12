# list comprehension
## with for loop
# numbers = [1, 2, 3]
# new_list = []
# for n in numbers:
#     add_1 = n + 1
#     new_list.append(add_1)
# print(new_list)

# # with list comprehension
# new_list = [n + 1 for n in numbers]
# print(new_list)

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# #  Do Not Change the code above 

# #Write your 1 line code  below:
# squared_numbers = [num * num for num in numbers]


# #Write your code  above:

# print(squared_numbers)

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# #  Do Not Change the code above
# #Write your 1 line code  below:

# result = [num for num in numbers if num % 2 == 0]

# #Write your code  above:

# print(result)

# with open("day_26/file1.txt") as file1:
#     file1_data = file1.readlines()
# # file1 = [int(num.strip()) for num in file1]
# print(file1)

# with open("day_26/file2.txt") as file2:
#     file2_data = file2.readlines()
# #file2 = [int(num.strip()) for num in file2]
# print(file2)

# result = [int(num) for num in file1_data if num in file2_data]
# print(result)
# import random
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# student_score = {student:random.randint(50,100) for student in names}
# print(student_score)

# passed_students = {student:score for (student, score) in student_score.items() if score > 60}
# print(passed_students)

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# # Don't change code above 👆

# # Write your code below:
# result = {word:len(word) for word in sentence.split()}
# print(result)

# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# # 🚨 Don't change code above 👆


# # Write your code 👇 below:

# weather_f = {day:((temp_c * 9/5) + 32) for (day, temp_c) in weather_c.items()}

# print(weather_f)

import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# for (key, value) in student_dict.items():
#     print(value)

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# for (key, value) in student_data_frame.items():
#     print(value)

#pandas built-in loop --> iterrows
# loop through rows of dataframe
for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)