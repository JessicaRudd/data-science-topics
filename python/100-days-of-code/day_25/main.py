import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US States Game")
image = "day_25/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_data = pd.read_csv("day_25/50_states.csv")
states_list = states_data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:

    answer_state = (screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?")).title()

    if answer_state == "Exit":

        missing_states = [state for state in states_list if state not in guessed_states]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("day_25/states_to_learn.csv")
        break
        
    if answer_state in states_list:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state = states_data[states_data.state == answer_state]
        t.goto(int(state.x), int(state.y))
        t.write(answer_state)


## A way to get the x and y values of the states from the gif by clicking on each state
# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
# turtle.exitonclick()

