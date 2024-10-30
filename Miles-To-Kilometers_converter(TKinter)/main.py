from tkinter import *

def convert():
    try:
        miles = float(entry.get())
        kilometers = round(miles * 1.60934, 1)
        label_3.config(text=kilometers)
    except ValueError:
        label_3.config(text="Invalid input")

window = Tk()
window.config(padx = 20, pady = 20)
window.title("Mile to Km Converter")

#Entry for Miles to convert
entry = Entry(width = 10)
entry.grid(column = 1 , row = 0)
entry.insert(END, string = str(0))
entry.focus()

# Label for Miles text next to the entry window
miles_label = Label(text = "Miles")
miles_label.grid(column = 2, row = 0)

# Label for conversion beginning
label_2 = Label(text = "is equal to")
label_2.grid(column = 0, row = 1)

# Label to show converted miles to km
label_3 = Label(text = 0) # add here the result of the calculus
label_3.grid(column = 1, row = 1)

# Label to mark the KM
label_4 = Label(text = "Km")
label_4.grid(column = 2, row = 1)

# Action Button
button = Button(text = "Calculate", command = convert)
button.grid(column = 1, row = 3)


window.mainloop()