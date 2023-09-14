from tkinter import *
from tkinter import messagebox
import random
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password = ""

def generate():
  nr_letters = random.randint(8, 10)
  nr_symbols = random.randint(2, 4)
  nr_numbers = random.randint(2, 4)

  password_list = []

  for char in range(nr_letters):
    password_list.append(random.choice(letters))

  for char in range(nr_symbols):
    password_list += random.choice(symbols)

  for char in range(nr_numbers):
    password_list += random.choice(numbers)

  random.shuffle(password_list)

  password = ""
  for char in password_list:
    password += char

  password_entry.delete(0, END)
  password_entry.insert(0, password)

  window.clipboard_clear()
  window.clipboard_append(password)

  messagebox.showinfo(title="website", message="password copied to clipboard")

def search():
   pass

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    website = website_entry.get()
    email= email_entry.get()
    password = password_entry.get()
    new_data = {
       website: {
          "email" : email,
          "password" : password
       }
    }

    if len(website) < 1 or len(password) < 1:
        messagebox.showinfo(title="website", message="Please fill the details first")
    else:
        is_ok = messagebox.askokcancel(title="Website", message=f"These are the entered details:\nemail: {email} \npassword: {password} \n Is it ok to save?")

        if is_ok:
          try:
            with open("data.json", "r") as datafile:
              # Reading old data
              data = json.load(datafile) 
          except FileNotFoundError:
            with open("data.json", "w") as datafile:
              json.dump(new_data, datafile, indent=4)            
          
          else:
            data.update(new_data)

            with open("data.json", "w") as datafile:
              json.dump(data, datafile, indent=4)            
        
          finally:
              website_entry.delete(0, END)
              password_entry.delete(0, END)
            
def search():
  try:
    with open("data.json", "r") as datafile:
      check_data = json.load(datafile)
  except FileNotFoundError:
    messagebox.showerror(title="website", message="No Data Found")
  else:
    try:
      email = check_data[website_entry.get()]['email']
      password = check_data[website_entry.get()]['password']
    except KeyError:
      messagebox.showinfo(title="website", message=f'no details found')
    messagebox.showinfo(title="website", message=f'email: {email} \npassword: {password}')
  

              
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=21)
website_entry.focus()
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=39)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "Mohit@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
search_btn = Button(text='Search', width=14, command=search)
search_btn.grid(column=2, row=1)
generate_password_button = Button(text="Generate Password", width=14, command=generate)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=add)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()