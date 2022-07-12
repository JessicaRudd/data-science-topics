import tkinter

## Buttons
# Event listener
def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609344, 2)
    result_label.config(text=f"{km}")

window = tkinter.Tk()
window.title("Mile to KM Converter")
# window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# # Entry component

miles_input = tkinter.Entry(width=7)
#Puts cursor in textbox.
miles_input.focus()
#Add some text to begin with
miles_input.insert(tkinter.END, 0)
miles_input.grid(column=1, row=0)

# Labels
miles_label = tkinter.Label(text="Miles", font = ("Arial", 24, "bold"))
miles_label.grid(column=2 , row=0)
#miles_label.config(padx=50, pady=50)

equal_label = tkinter.Label(text="is equal to", font = ("Arial", 24, "bold"))
equal_label.grid(column=0 , row=1)
#equal_label.config(padx=50, pady=50)

km_label = tkinter.Label(text="Km", font = ("Arial", 24, "bold"))
km_label.grid(column=2 , row=1)
#km_label.config(padx=50, pady=50)

result_label = tkinter.Label(text=0, font = ("Arial", 24, "bold"))
result_label.grid(column=1, row=1)

## Buttons
button = tkinter.Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)



window.mainloop()

