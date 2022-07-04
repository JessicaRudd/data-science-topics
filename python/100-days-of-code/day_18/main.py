#####Turtle Intro######
#from turtle import Screen, Turtle, shape
import random
import turtle as t

# timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("blue")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)

# screen = t.Screen()
# screen.exitonclick()

######## Challenge 1 - Draw a Square ############
# turtle = Turtle()
# turtle.shape("turtle")
# turtle.color("blue")
# for _ in range(4):
#     turtle.forward(100)
#     turtle.right(90)

# screen = Screen()
# screen.exitonclick()


########### Challenge 2 - Draw a Dashed Line ########
# turtle = Turtle()
# turtle.shape("turtle")
# turtle.color("purple")

# def motion():
#     turtle.forward(10)

# for _ in range(15):
#     motion()
#     turtle.penup()
#     motion()
#     turtle.pendown()

########### Challenge 3 - Draw Shapes ########
# colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

# t = Turtle()
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         t.forward(100)
#         t.right(angle)

# for shape_side_n in range(3,10):

#     t.color(random.choice(colors))
#     draw_shape(shape_side_n)

########### Challenge 4 - Random Walk ########
# tim = Turtle()
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"] 
# directions = [0, 90, 180, 270]
# tim.pensize(15)
# tim.speed("fastest")

# for _ in range(200):
#     tim.color(random.choice(colours))
#     tim.forward(30)
#     tim.setheading(random.choice(directions))


tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

# directions = [0, 90, 180, 270]
# tim.pensize(15)
tim.speed("fastest")

# for _ in range(200):

#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

########### Challenge 5 - Spirograph ########

def draw_spirograph(size_of_gap):

    # Radius
    r = 100
    for _ in range(int(360 / size_of_gap)):    
        tim.color(random_color())
        tim.circle(r)
        tim.seth(tim.heading() + 10)

draw_spirograph(5)
screen = t.Screen()
screen.exitonclick()