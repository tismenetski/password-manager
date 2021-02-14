import json
from tkinter import * # Import classes and constants
from tkinter import messagebox # this is simply a module
import random
import itertools

# ---------------------------- CONSTANTS ------------------------------- #
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    passwordList = []
    password_letters = [random.choice(LETTERS) for _ in range(nr_letters)]
    password_symbols = [random.choice(SYMBOLS) for _ in range(nr_symbols)]
    password_numbers = [random.choice(NUMBERS) for _ in range(nr_numbers)]
    passwordList = password_numbers + password_symbols + password_letters

    random.shuffle(passwordList)
    password = ''.join(passwordList)

    password_entry.delete(0,END)
    password_entry.insert(0,password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    password = password_entry.get()
    email = email_entry.get()
    website = website_entry.get()
    new_data = {
        website: {
        "email": email,
        "password": password
    }
    }
    if password and website:
        with open('passwords.json','r') as file: # a - append to the end of the file
            data = json.load(file) # Read Data from a JSON File
            data.update(new_data) # Update JSON with new data

        with open('passwords.json', 'w') as file:
            json.dump(data, file, indent=4)  # Write data to JSON File

        clean_entries()
    else:
        messagebox.showinfo(title="warning",message="One of the fields is empty, please fill all the fields")

def clean_entries():
    website_entry.delete(0,END)
    password_entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx = 50, pady = 50)

# ----------------------------- CANVAS --------------------------------- #
canvas = Canvas(width = 200, height = 200)
photo_image=PhotoImage(file = "logo.png")
canvas.create_image(100, 100, image = photo_image)
canvas.grid(column = 1,row = 0)


# ---------------------------- LABELS ------------------------------- #

website_label = Label(text = "Website:")
website_label.grid(row = 1, column = 0)

email_label = Label(text = "Email/Username:")
email_label.grid(row = 2, column = 0)

password_label = Label(text = "Password:")
password_label.grid(row = 3, column = 0)

# ---------------------------- INPUTS ------------------------------- #

website_entry = Entry(width = 35)
website_entry.grid(row = 1, column = 1 , columnspan = 2)
website_entry.focus() # Puts the cursor on the specific entry

email_entry = Entry(width = 35)
email_entry.insert(0,"tismenetski@gmail.com") # pre-populate a field
email_entry.grid(row = 2, column = 1 , columnspan = 2)

password_entry = Entry(width = 21)
password_entry.grid(row = 3, column = 1)

# ---------------------------- BUTTONS ------------------------------- #
generate_password_button = Button(text="Generate Password", command= generate_password)
generate_password_button.grid(row = 3, column = 2)

add_button = Button(text= "Add", width = 36 , command = save_password)
add_button.grid(row = 4 , column = 1,  columnspan = 2 )




window.mainloop()