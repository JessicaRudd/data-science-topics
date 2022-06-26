# # Functions with outputs

# def format_name(f_name, l_name):

#     full_name = f_name.title() + " " + l_name.title()
#     return full_name

# print(format_name("jessica", "rudd"))

# # Functions with multiple outputs

# def format_name(f_name, l_name):
#     """Take a first and last name and format it to title case.

#     Args:
#         f_name (string): first name from user input
#         l_name (string): last name from user input

#     Returns:
#         string: first and last name in title case, appended together
#     """
#     if f_name == "" or l_name == "":
#         return "You didn't provide valid inputs."

#     full_name = f_name.title() + " " + l_name.title()
#     return f"Result: {full_name}"

# print(format_name(input("What is your first name? "), input("What is your last name? ")))


def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
    if month > 12 or month < 1:
        return "Invalid month."
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
    if is_leap(year) and month == 2:
        return 29

    return month_days[month - 1]
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
