# with open("day_25/weather_data.csv") as weather_file:
#     data = weather_file.readlines()
#     print(data)

# import csv

# with open("day_25/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# import pandas as pd

# data = pd.read_csv("day_25/weather_data.csv")
# avg = max(data["temp"])
# print(avg)

# # Get data in columns
# print(data["condition"])
# print(data.condition)

# # Get data in row
# print(data[data.day == "Monday"])

# # Get row with highest temp
# high_temp = data[data.temp == data.temp.max()]
# print(high_temp)

# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_f = monday_temp * 9/5 + 32
# print(monday_temp_f)

# Create df from scratch
# squirrels = pd.read_csv("day_25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# # print(squirrels.columns)
# squirrel_count = pd.DataFrame(squirrels["Primary Fur Color"].value_counts())
# print(squirrel_count)

# gray_squirrels_count = len(squirrels[squirrels["Primary Fur Color"] == "Gray"])
# print(gray_squirrels_count)

# red_squirrels_count = len(squirrels[squirrels["Primary Fur Color"] == "Cinnamon"])
# print(red_squirrels_count)

# black_squirrels_count = len(squirrels[squirrels["Primary Fur Color"] == "Black"])
# print(black_squirrels_count)

# data_dict = {
#     "Fur Color": ["Gray", "Cinnamon", "Black"],
#     "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
#     }

# df = pd.DataFrame(data_dict)
# df.to_csv("squirrel_count.csv")