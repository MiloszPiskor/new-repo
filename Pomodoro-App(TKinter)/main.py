from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps
    global ticks
    reps = 0
    ticks = ""
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label_timer.config(text="Timer", fg=GREEN)
    label_tick.config(text=ticks)



# ---------------------------- TIMER MECHANISM ------------------------------- #
ticks = ""
def start_timer():
    global reps
    global ticks
    reps += 1
    if reps > 8:
        reps = 0  # Reset reps after 8 rounds
        ticks = ""
        return
    if reps == 8:
        label_timer.config(text = "Long break time!!!", fg = RED)
        countdown(LONG_BREAK_MIN * 60)
        ticks += "✔"
        label_tick.config(text = ticks)
    elif reps % 2 == 0 and reps != 8:
        label_timer.config(text="Short break!", fg = PINK)
        countdown(SHORT_BREAK_MIN * 60)
        ticks += "✔"
        label_tick.config(text = ticks)
    elif reps % 2 != 0:
        label_timer.config(text="Time to work!", fg = GREEN)
        countdown(WORK_MIN * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):

    first_num = int(count / 60)
    second_num = count % 60
    if second_num < 10:
        second_num = f"0{second_num}"

    canvas.itemconfig(timer_text, text = f"{first_num}:{second_num}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1) # takes the function with inputs, positional arguments
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx= 100, pady = 70, bg = YELLOW)
window.title("Pomodoro App")


canvas = Canvas(width=200, height=224, bg = YELLOW, highlightthickness = 0)
pomodoro = PhotoImage(file = "tomato.png") # A way to read through a file
canvas.create_image(100, 112, image = pomodoro )
timer_text = canvas.create_text(100, 130, text = "00:00", font = (FONT_NAME ,35, "bold"), fill = "white")
canvas.grid(column = 1, row = 1)

button_start = Button(text = "Start", bg = YELLOW, highlightthickness = 0, command = start_timer)
button_start.grid(column = 0, row = 3)

button_reset = Button(text = "Reset", bg = YELLOW, highlightthickness = 0, command = reset_timer)
button_reset.grid(column = 2, row = 3)

label_timer = Label(text = "Timer", fg = GREEN, bg = YELLOW, font = ("Courier", 35, "bold"))
label_timer.grid(column = 1, row = 0)

label_tick = Label(fg = GREEN,bg = YELLOW, font = 10)
label_tick.grid(column = 1, row = 4)  # ADD WHEN NEEDED

window.mainloop()

