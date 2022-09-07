import smtplib
import os
import datetime as dt
import random
import pandas as pd
from dotenv import load_dotenv

project_folder = os.path.expanduser('.')
load_dotenv(os.path.join(project_folder, '.env'))

EMAIL_USER = os.getenv("EMAIL")
EMAIL_PASSWORD = os.getenv("EMAIL_APP_PW")
SUBJECT = "Happy Birthday!"

now = dt.datetime.now()
today_tuple = (now.month, now.day)
data = pd.read_csv("birthdays.csv")
birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    rand_int = random.randint(1,3)
    file_path = f"letter_templates/letter_{rand_int}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL_USER, password=EMAIL_PASSWORD)
        connection.sendmail(
            from_addr=EMAIL_USER, 
            to_addrs=birthday_person["email"], 
            msg=f"Subject:{SUBJECT}\n\n{contents}")











