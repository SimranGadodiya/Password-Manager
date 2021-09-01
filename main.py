from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    input2.insert(0, f"{password}")
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = input.get()
    email = input1.get()
    password = input2.get()
    new_data = {website.title():
        {
            "email": email,
            "password": password,
        }
    }
    if website == "" or password == "":
        messagebox.showwarning(title="Warning", message="Fields cant be empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"You have entered: \n Email: {email}\n"
                                                              f"Password: {password}\nIs it Ok ?")
        if is_ok:
            try:
                with open("data.json", "r") as file:
                    # Reading data
                    data = json.load(file)
            except:
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                # Updating old data with new
                data.update(new_data)
                with open("data.json", "w") as file:
                    # Saving Updated data
                    json.dump(data, file, indent=4)
            finally:
                input.delete(0, END)
                input2.delete(0, END)


# ---------------------------- Search Function ------------------------------- #
def find_password():
    website = input.get().title()
    try:
        with open("data.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="Data Not Found!😢")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details found for {website}.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=20, pady=20)
window.title("Password Generator")

canvas = Canvas(height=200, width=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

web_lab = Label(text="Website :")
web_lab.grid(row=1, column=0)

input = Entry(width=32)
input.grid(column=1, row=1)
input.focus()

mail_lab = Label(text="Email/Username: ")
mail_lab.grid(column=0, row=2)

input1 = Entry(width=50)
input1.grid(column=1, row=2, columnspan=2)
input1.insert(0, "simran@gmail.com")

pass_lab = Label(text="Password: ")
pass_lab.grid(column=0, row=3)

input2 = Entry(width=32)
input2.grid(column=1, row=3)

button = Button(text="Search", width=13, command=find_password)
button.grid(column=2, row=1)
button = Button(text="Generate Password", width=14, command=generate_password)
button.grid(column=2, row=3)

button = Button(text="Add", width=42, command=save)
button.grid(column=1, row=4, columnspan=2)
window.mainloop()
