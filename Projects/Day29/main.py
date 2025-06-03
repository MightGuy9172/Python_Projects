from tkinter import *
from tkinter import messagebox
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
import random

def generate_paasword():
    password_entry.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(4, 5))]
    password_symbol = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_number = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list=password_letters+password_number+password_symbol
    random.shuffle(password_list)

    random_paas = "".join(password_list)
    password_entry.insert(0,random_paas)
    pyperclip.copy(random_paas)


# ---------------------------- FIND PASSWORD ------------------------------- #


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    web=website_entry.get()
    password=password_entry.get()
    email=email_entry.get()

    if len(web)==0 or len(password)==0:
        messagebox.showinfo(title="OOPS !",message="Please Fill the details.")
    else:
        is_ok=messagebox.askokcancel(title=web,message=f"These are the details: Email-{email} and Password-{password}.\n Is it ok to save?")
        if is_ok:
            with open("data.txt","a") as file:
                file.write(f"{web}  | {email} | {password}")
                website_entry.delete(0,END)
                password_entry.delete(0,END)




#---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(pady=20,padx=20)

canvas=Canvas(width=200,height=200)
img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=img)
canvas.grid(column=1,row=0)

#Website
websiteLabel=Label(text="Website:")
websiteLabel.grid(column=0,row=1)
website_entry=Entry(width=35)
website_entry.focus()
website_entry.grid(column=1,row=1,columnspan=2,sticky="W")


#Email/Username
emailLabel=Label(text="Email/Username:")
emailLabel.grid(column=0,row=2)
email_entry=Entry(width=35)
email_entry.grid(column=1,row=2,columnspan=2,sticky="W")

#Password
passLabel=Label(text="Password:")
passLabel.grid(column=0,row=3)
password_entry=Entry(width=21)
password_entry.grid(column=1,row=3,sticky="W")
generate=Button(text="Generate Password",width=14,command=generate_paasword)
generate.grid(column=1,row=3,sticky="E")



#Add
addData=Button(text="Add",width=35,command=save_password)
addData.grid(column=1,row=4,columnspan=2,sticky="W")




window.mainloop()