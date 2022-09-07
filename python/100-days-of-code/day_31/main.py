from tkinter import *
from PIL import Image, ImageTk
import sys, os
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

current_card = {}

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
        for k, v in os.environ.items():
            print(f'{k}={v}')
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    print('running in a PyInstaller bundle')
    DATA_PATH = resource_path('data')

else:
    print('running in a normal Python process')
    DATA_PATH = resource_path('data')

## Next Card
def next_card():
    global current_card, flip_timer
    # Reset timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, flip_card)

## Flip card
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)

## update list of words
def is_known():
    to_learn.remove(current_card)

    data = pandas.DataFrame(to_learn)
    data.to_csv("./data/words_to_learn.csv", index=False)
    next_card()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

## Wait 3 seconds
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front = Image.open(resource_path("./images/card_front.png"))
card_front_img = ImageTk.PhotoImage(card_front)
card_back = Image.open(resource_path("./images/card_back.png"))
card_back_img = ImageTk.PhotoImage(card_back)
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 264, font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

#Buttons
correct_button_img = Image.open(resource_path("./images/right.png"))
right_img = ImageTk.PhotoImage(correct_button_img)
correct_button = Button(image=right_img, highlightthickness=0, command=is_known)
correct_button.grid(column=0, row=1)

wrong_button_img = Image.open(resource_path("./images/wrong.png"))
wrong_img = ImageTk.PhotoImage(wrong_button_img)
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(column=1, row=1)

next_card()

window.mainloop()