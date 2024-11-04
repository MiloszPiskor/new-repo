from tkinter import *
from tkinter import messagebox
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def create_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    user_password = [random.choice(letters) for _ in range(random.randint(8,10))]
    user_password.extend([random.choice(symbols) for _ in range(random.randint(2,4))])
    user_password.extend([random.choice(numbers) for _ in range(random.randint(2,4))])

    random.shuffle(user_password)

    output = "".join(user_password)

    entry_3.delete(0, END)
    entry_3.insert(0, output)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    website = entry_1.get()
    e_mail = entry_2.get()
    password = entry_3.get()

    if len(website) == 0 or len(password) == 0:

        messagebox.showerror(title="Blimey!", message="You shouldn't leave any field empty!")
        return

    is_ok = messagebox.askokcancel(title = f"{website}", message = f"These are the information you've entered:\n"
                                                           f"E-mail: {e_mail}\n Password: {password}\n Do you want to proceed?")

    if is_ok:
        with open("data.txt", mode  = "a+") as file:
            file.write(f"{website} | {e_mail} | {password}\n")
        entry_1.delete(0, END)
        entry_3.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(width = 300, height = 300, padx = 30, pady = 30)

# Canvas object- a logo for the app:
canvas = Canvas(width = 200, height = 200)
our_lock = PhotoImage(file = "logo.png")
picture = canvas.create_image(100, 100, image = our_lock)
canvas.grid(column = 1,row = 0, padx = 20, pady = 20)

#Name Labels labelling the entry windows:
label_1 = Label(text = "Website:")
label_1.grid(column = 0, row = 1)
label_2 = Label(text = "Email/Username:")
label_2.grid(column = 0, row = 2)
label_3 = Label(text = "Password:")
label_3.grid(column = 0, row = 3)

# Entries for user inputs:
website = StringVar()
entry_1 = Entry(textvariable= website, width = 60)
entry_1.grid(column = 1, row = 1, columnspan = 2)
entry_1.focus()

email_username = StringVar()
entry_2 = Entry(textvariable= email_username, width = 60)
entry_2.grid(column = 1, row = 2, columnspan = 2)
entry_2.insert(0, "milosz11@vp.pl")

password = StringVar()
entry_3 = Entry(textvariable= password, width= 41)
entry_3.grid(column = 1, row = 3)

# Buttons:
generate_password = Button( text = "Generate Password", command = create_password)
generate_password.grid(column = 2, row = 3)
add = Button( text = "Add", width = 51, command = save)
add.grid(column = 1, row = 4, columnspan = 2)

window.mainloop()