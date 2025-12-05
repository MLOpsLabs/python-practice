
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import re

root = Tk()
root.title("Login Form")
root.geometry("420x520")
root.configure(background="#e0f7fa")

# Set window icon
icon = PhotoImage(file="gui/favicon.png")
root.iconphoto(False, icon)

# Load and resize logo
img = Image.open("gui/yuktiio-logo-new.png")
img = img.resize((160, 45), Image.Resampling.LANCZOS)
img_tk = ImageTk.PhotoImage(img)

# Main Frame
frame = Frame(root, bg="#e0f7fa")
frame.pack(expand=True)

# Logo
img_label = Label(frame, image=img_tk, bg="#e0f7fa")
img_label.pack(pady=(20, 10))

txt_label = Label(frame, text="Welcome to Yuktiio", font=("Helvetica", 18, "bold"), fg="#37474f", bg="#e0f7fa")
txt_label.pack(pady=(0, 20))

# Email
email_label = Label(frame, text="Email", font=("Helvetica", 12), fg="#37474f", bg="#e0f7fa")
email_label.pack(anchor="w", padx=40)
email_input = Entry(frame, font=("Helvetica", 12), width=30, relief="solid", bd=1)
email_input.pack(pady=(5, 15))

# Password
password_label = Label(frame, text="Password", font=("Helvetica", 12), fg="#37474f", bg="#e0f7fa")
password_label.pack(anchor="w", padx=40)
password_input = Entry(frame, font=("Helvetica", 12), width=30, show="*", relief="solid", bd=1)
password_input.pack(pady=(5, 10))

# Show/Hide Password
def toggle_password():
    if password_input.cget('show') == '*':
        password_input.config(show='')
        toggle_btn.config(text="Hide")
    else:
        password_input.config(show='*')
        toggle_btn.config(text="Show")

toggle_btn = Button(frame, text="Show", font=("Helvetica", 10), bg="#b2dfdb", fg="#37474f", command=toggle_password)
toggle_btn.pack(pady=(0, 15))

# Remember Me
remember_var = IntVar()
remember_check = Checkbutton(frame, text="Remember Me", variable=remember_var, bg="#e0f7fa", fg="#37474f", font=("Helvetica", 10))
remember_check.pack(anchor="w", padx=40)

# Forgot Password
forgot_btn = Button(frame, text="Forgot Password?", font=("Helvetica", 10, "underline"), bg="#e0f7fa", fg="#00796b", bd=0)
forgot_btn.pack(anchor="e", padx=40, pady=(5, 15))

# Login Button with hover effect
def on_enter(e):
    login_button.config(bg="#004d40")

def on_leave(e):
    login_button.config(bg="#00796b")

def validate_login():
    email = email_input.get().strip()
    password = password_input.get().strip()
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        messagebox.showerror("Invalid Email", "Please enter a valid email address.")
    elif len(password) < 6:
        messagebox.showerror("Invalid Password", "Password must be at least 6 characters.")
    else:
        messagebox.showinfo("Login Successful", f"Welcome, {email}!")

login_button = Button(frame, text="Login", font=("Helvetica", 12, "bold"), bg="#00796b", fg="#ffffff", width=20, command=validate_login)
login_button.pack(pady=(20, 10))
login_button.bind("<Enter>", on_enter)
login_button.bind("<Leave>", on_leave)

root.mainloop()
