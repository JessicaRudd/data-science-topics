# Local vs global scope
################### Scope ####################

# enemies = 1

# def increase_enemies():
#   enemies = 2
#   print(f"enemies inside function: {enemies}")
#   #this prints 2

# increase_enemies()
# print(f"enemies outside function: {enemies}")
#this prints 1

# # Local scope - exists within functions
# def drink_potion():

#     potion_strength = 2
#     print(potion_strength)

# drink_potion() # -> this will print the local scope var potion_strenght = 2

# print(potion_strength) # -> this will produce an error because potion_strenght is a local scope var and not accesible outside function

# # Global scope
# player_health = 10
# def drink_potion():

#     potion_strength = 2
#     print(player_health) # -> this is available inside the func because it was defined globally

# # both of these will work
# drink_potion()
# print(player_health)

# # There is no block scope
# game_level = 3
# enemies = ["skeletons","zombies","aliens"]

# if game_level < 5:
#     #this will be available at global scope
#     #but if we embed this in a function it will become local scope and then no longer work
#     new_enemy = enemies[0]

# print(new_enemy)

# # Modifying global scope
# enemies = 1

# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")

# modify global scope var - not recommended - should define global and local vars differently
# its best to avoid modifying global scope variables
# enemies = 1

# def increase_enemies():
#     global enemies
#     enemies += 1
#     print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")

# # Better to use return
# enemies = 1

# def increase_enemies():
#     print(f"enemies inside function: {enemies}")
#     return enemies + 1

# enemies = increase_enemies()
# print(f"enemies outside function: {enemies}")

# Global constants - convention to name it with all uppercase

PI = 3.14159
URL = "http://www.google.com"
TWITTER_HANDLE = "@funsizeathlete"


