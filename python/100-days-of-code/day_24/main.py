# file = open("day_24/my_file.txt")
# # using "with" manages file and do not have to remember to close file
# with open("day_24/my_file.txt") as file:
#     contents = file.read()
#     print(contents)
# # "a" to append new text, "w" is write mode and will overwrite
# with open("./my_file.txt", mode="a") as file:
#     file.write("\nNew text.")

# # Write to a new file
# with open("day_24/new_file.txt", mode="w") as file:
#     file.write("\nNew text.")


#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
PLACEHOLDER = "[name]"
with open("day_24/Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()


with open("day_24/Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    #print(letter)

for name in names:
    stripped_name = name.strip()
    new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
    with open(f"day_24/Output/ReadyToSend/letter_for_{stripped_name}", mode="w") as completed_letter:
        completed_letter.write(new_letter)