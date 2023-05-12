from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
	website=website_entry.get()
	email=email_entry.get()
	password=password_entry.get()

	if len(website)==0 or len(password)==0:
		messagebox.showwarning(message="Please do not leave any field empty.")
		

	is_ok=messagebox.askokcancel(title=website,message=f"The entered informaion is:\nwebsite:{website}\nEmail:{email}\nPassword:{password}\nDo you want to save ?")

	if is_ok:
		with open("data.txt","a") as f:
			f.write(f"{website} | {email} | {password}\n")
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

generate_password=Button(text="Generate Password")
generate_password.grid(column=2,row=3)

add_button=Button(text="Add",width=36,command=save)
add_button.grid(column=1,row=4,columnspan=2)

window.mainloop()