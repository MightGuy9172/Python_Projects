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
def search_data():
    website_search=website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            if website_search in data:
                found_email=data[website_search]["email"]
                found_pass = data[website_search]["password"]
                messagebox.showinfo(title=website_search,message=f"Your email={found_email}\nYour password={found_pass}")
            else:
                messagebox.showinfo(title=website_search, message=f"No Data is Available")
    except FileNotFoundError:
        messagebox.showinfo(title=website_search, message="DataBase Not Found !")
    finally:
        website_entry.delete(0, END)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    web=website_entry.get()
    password=password_entry.get()
    email=email_entry.get()

    new_data={
        web:{
            "email":email,
            "password":password,
        }
    }

    if len(web)==0 or len(password)==0:
        messagebox.showinfo(title="OOPS !",message="Please Fill the details.")
    else:
        is_ok=messagebox.askokcancel(title=web,message=f"These are the details: Email-{email} and Password-{password}.\n Is it ok to save?")
        if is_ok:
            try:
                with open("data.json","r") as data_file:
                    data=json.load(data_file)
            except FileNotFoundError:
                with open("data.json","w") as data_file:
                    json.dump(new_data,data_file , indent=4)
            else:
                data.update(new_data)
                with open("data.json","w") as data_file:
                    json.dump(data,data_file , indent=4)
            finally:
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
website_entry=Entry(width=19)
website_entry.focus()
website_entry.grid(column=1,row=1,columnspan=1,sticky="W")
search=Button(text="Search",width=13,command=search_data)
search.grid(column=1,row=1,sticky="E")


#Email/Username
emailLabel=Label(text="Email/Username:")
emailLabel.grid(column=0,row=2)
email_entry=Entry(width=35)
email_entry.grid(column=1,row=2,columnspan=2,sticky="W")

#Password
passLabel=Label(text="Password:")
passLabel.grid(column=0,row=3)
password_entry=Entry(width=19)
password_entry.grid(column=1,row=3,sticky="W")
generate=Button(text="Generate Password",width=13,command=generate_paasword)
generate.grid(column=1,row=3,sticky="E")



#Add
addData=Button(text="Add",width=29,command=save_password)
addData.grid(column=1,row=4,columnspan=2,sticky="W")




window.mainloop()