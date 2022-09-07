import smtplib
import os
import datetime as dt
import random
from dotenv import load_dotenv

project_folder = os.path.expanduser('.')
load_dotenv(os.path.join(project_folder, '.env'))

now = dt.datetime.now()
day_of_week = now.weekday()

EMAIL_USER = os.getenv("EMAIL")
EMAIL_PASSWORD = os.getenv("EMAIL_APP_PW")
SUBJECT = "Morning Motivation!"

def random_line(txt_file):
    lines = open(txt_file).readlines()
    return random.choice(lines)

def email_list(email_file):
    content = open(email_file).readlines()
    email_list = [line.strip() for line in content]
    return email_list

# if day_of_week == 1:
text = random_line("quotes.txt")

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=EMAIL_USER, password=EMAIL_PASSWORD)
    connection.sendmail(
        from_addr=EMAIL_USER, 
        to_addrs=email_list("emails.txt"), 
        msg=f"Subject:{SUBJECT}\n\n{text}")
