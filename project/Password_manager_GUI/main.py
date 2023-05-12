from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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

email_label=Label(text="Email/Username:")
email_label.grid(column=0,row=2)

email_entry=Entry(width=39)
email_entry.grid(column=1,row=2,columnspan=2)

password_label=Label(text="Password:")
password_label.grid(column=0,row=3)

password_entry=Entry(width=21)
password_entry.grid(column=1,row=3)

generate_password=Button(text="Generate Password")
generate_password.grid(column=2,row=3)

add_button=Button(text="Add",width=36)
add_button.grid(column=1,row=4,columnspan=2)

window.mainloop()