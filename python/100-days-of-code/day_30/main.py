## Errors and exceptions

# #File not found
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key":"value"}
#     a_dictionary["asdfadsf"]

# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("something")

# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")

# else:
#     content = file.read()
#     print(content)

# finally:
#     raise KeyError
    # file.close()
    # print("The file was closed.")

#KeyError
# a_dictionary = {"key":"value"}
# value = a_dictionary["non_existent_key"]

#IndexError
# fruit_list = ["Apple","Banana","Pear"]
# fruit = fruit_list[3]

#TypeError
# text = "abc"
# print(text + 5)

## Raising exceptions
# height = float(input("Height: "))
# weight = int(input("Weight "))

# bmi = weight / height ** 2
# print(bmi)

# if height > 3:
#     raise ValueError("Human height should not be over 3 meters")



