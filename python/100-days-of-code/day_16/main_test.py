## Object oriented programming OOP 
## Each task, like a job in a restaurant, requires: what it has (attributes, i.e. variable associated with this method), \
#                                                   what it does (methods, i.e. actions/functions that a task can do)
## Object tasks, blueprints for these tasks are called 'Classes'
## Can generate many custom objects from these Classes
## Classes are denoted with pascal class
## A package is a bunch of modules together
# import another_module
from prettytable import PrettyTable
# from turtle import Turtle, Screen

# # print(another_module.another_variable)

# timmy = Turtle()
# print(timmy)
# #Call methods of the Turtle class
# timmy.shape("turtle")
# timmy.color("DarkMagenta")
# timmy.forward(100)
# my_screen = Screen()

# # Get canvheight attribute from my_screen object
# # print(my_screen.canvheight)

# my_screen.exitonclick()

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu","Squirtle","Charmander"])
table.add_column("Type", ["Electric","Water","Fire"])
table.align["Pokemon Name"] = "l"
table.align = "l"
print(table)




