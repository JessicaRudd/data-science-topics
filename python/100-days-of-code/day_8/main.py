# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.
# paramater is name of value, argument is the dynamic value of that parameter

# def greet():

#     print("Hello")
#     print("How do you do?")
#     print("Isn't the weather nice today?")

# greet()

# Function that allows input

# def greet_with_name(name):
    
#     print(f"Hello {name}")
#     print(f"How do you do, {name} ")
#     print("Isn't the weather nice today?")

# greet_with_name("Jessica")

#Fucntions with more than 1 input/argument
#name and location are positional arguments
# keywork arguments are more explicit, i.e. a=1, b=2 vs 1, 2
# def greet_with(name, location):

#     print(f"Hello {name}")
#     print(f"What is it like in {location}")

# greet_with("Jessica", "Atlanta")

#with keyword args
def greet_with(name, location):

    print(f"Hello {name}")
    print(f"What is it like in {location}")

greet_with(name="Jessica", location="Atlanta")
