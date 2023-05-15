from tkinter import *
from tkinter import messagebox
import random
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project

def insert_random_password():
	letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

	nr_letters= random.randint(0,10)
	nr_symbols = random.randint(0,4)
	nr_numbers = random.randint(0,4)

	password_letter=[random.choice(letters) for _ in range(nr_letters)]
	password_symbol=[random.choice(symbols) for _ in range(nr_symbols)]
	password_numbers=[random.choice(numbers) for _ in range(nr_numbers)]

	combination_password=password_letter+password_symbol+password_numbers
	random.shuffle(combination_password)

	random_password="".join(combination_password)

	password_entry.delete(0,END)
	password_entry.insert(0,f"{random_password}")

def find_password():
	try:
		with open("data.json","r") as data_file:
			data=json.load(data_file)
			website=website_entry.get()
			email=data[website]["email"]
			password=data[website]["password"]
	except KeyError:
		messagebox.showwarning(message="Entry not found.")
	else:
		messagebox.showinfo(title=website,message=f"email={email}\npassword={password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
	website=website_entry.get()
	email=email_entry.get()
	password=password_entry.get()

	new_data={website:{
	"email":email,
	"password":password
	}}

	if len(website)==0 or len(password)==0:
		messagebox.showwarning(message="Please do not leave any field empty.")
		return

	else:
		try:
			with open("data.json","r") as data_file:
				data=json.load(data_file)	#reading from the json file and and storing it in data
		except FileNotFoundError:
			with open("data.json","w") as data_file:
				json.dump(newdata,data_file)
		else:
			data.update(new_data)	#updating the newdata to the old data
			with open("data.json","w") as data_file:
				json.dump(data,data_file,indent=4)	#writing to the the json file
		finally:
			website_entry.delete(0,END)
			password_entry.delete(0,END)


# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password manager")
window.config(padx=50,pady=50)

canvas=Canvas(width=200,height=200)
lock_img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=lock_img)
canvas.grid(column=1,row=0)

website_label=Label(text="Website:")
website_label.grid(column=0,row=1)

website_entry=Entry(width=39)
website_entry.grid(column=1,row=1,columnspan=2)
website_entry.focus()

email_label=Label(text="Email/Username:")
email_label.grid(column=0,row=2)

email_entry=Entry(width=39)
email_entry.grid(column=1,row=2,columnspan=2)
email_entry.insert(0,"example@gmail.com")

password_label=Label(text="Password:")
password_label.grid(column=0,row=3)

password_entry=Entry(width=21)
password_entry.grid(column=1,row=3)

generate_password=Button(text="Generate Password",command=insert_random_password)
generate_password.grid(column=2,row=3)

add_button=Button(text="Add",width=36,command=save)
add_button.grid(column=1,row=4,columnspan=2)

search_button=Button(text="Search",command=find_password)
search_button.grid(column=3,row=1)

window.mainloop()