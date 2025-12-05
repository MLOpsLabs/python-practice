from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import re

root = Tk()
root.title("Login Form - Yuktiio")
root.geometry("420x580")
root.configure(background="#f8fafc")
root.resizable(False, False)

# Set window icon
try:
    icon = PhotoImage(file="gui/favicon.png")
    root.iconphoto(False, icon)
except:
    pass  # Continue without icon if file not found

# Colors
BG_COLOR = "#f8fafc"
PRIMARY_COLOR = "#00796b"
SECONDARY_COLOR = "#004d40"
ACCENT_COLOR = "#b2dfdb"
TEXT_COLOR = "#37474f"
ERROR_COLOR = "#f44336"
SUCCESS_COLOR = "#4caf50"
ENTRY_BG = "#ffffff"

# Main Frame
frame = Frame(root, bg=BG_COLOR)
frame.pack(expand=True, fill="both", padx=20, pady=20)

# Load and resize logo
try:
    img = Image.open("gui/yuktiio-logo-new.png")
    img = img.resize((180, 50), Image.Resampling.LANCZOS)
    img_tk = ImageTk.PhotoImage(img)
    
    # Logo
    img_label = Label(frame, image=img_tk, bg=BG_COLOR)
    img_label.pack(pady=(10, 15))
except:
    # If logo not found, show text instead
    logo_label = Label(frame, text="YUKTIIO", font=("Helvetica", 24, "bold"), 
                       fg=PRIMARY_COLOR, bg=BG_COLOR)
    logo_label.pack(pady=(10, 15))

# Welcome Text
welcome_label = Label(frame, text="Welcome Back", 
                      font=("Helvetica", 22, "bold"), fg=TEXT_COLOR, bg=BG_COLOR)
welcome_label.pack(pady=(0, 5))

subtitle_label = Label(frame, text="Sign in to your account", 
                       font=("Helvetica", 12), fg="#64748b", bg=BG_COLOR)
subtitle_label.pack(pady=(0, 30))

# Input Frame
input_frame = Frame(frame, bg=BG_COLOR)
input_frame.pack(padx=20)

# Email
email_frame = Frame(input_frame, bg=BG_COLOR)
email_frame.pack(fill="x", pady=(0, 15))

email_label = Label(email_frame, text="Email Address", font=("Helvetica", 11), 
                    fg=TEXT_COLOR, bg=BG_COLOR)
email_label.pack(anchor="w")

email_input = Entry(email_frame, font=("Helvetica", 12), width=35, 
                    relief="flat", bd=2, bg=ENTRY_BG, highlightthickness=1,
                    highlightbackground="#cbd5e1", highlightcolor=PRIMARY_COLOR)
email_input.pack(pady=(5, 0), ipady=8)
email_input.bind("<FocusIn>", lambda e: email_input.config(highlightbackground=PRIMARY_COLOR))
email_input.bind("<FocusOut>", lambda e: email_input.config(highlightbackground="#cbd5e1"))

# Email hint
email_input.insert(0, "you@example.com")
email_input.config(fg="#64748b")
def on_email_click(event):
    if email_input.get() == "you@example.com":
        email_input.delete(0, END)
        email_input.config(fg=TEXT_COLOR)
def on_email_leave(event):
    if email_input.get() == "":
        email_input.insert(0, "you@example.com")
        email_input.config(fg="#64748b")
email_input.bind("<FocusIn>", on_email_click)
email_input.bind("<FocusOut>", on_email_leave)

# Password
password_frame = Frame(input_frame, bg=BG_COLOR)
password_frame.pack(fill="x", pady=(0, 10))

password_label = Label(password_frame, text="Password", font=("Helvetica", 11), 
                       fg=TEXT_COLOR, bg=BG_COLOR)
password_label.pack(anchor="w")

password_input_container = Frame(password_frame, bg=BG_COLOR)
password_input_container.pack(fill="x", pady=(5, 0))

password_input = Entry(password_input_container, font=("Helvetica", 12), width=29, 
                       show="•", relief="flat", bd=2, bg=ENTRY_BG, highlightthickness=1,
                       highlightbackground="#cbd5e1", highlightcolor=PRIMARY_COLOR)
password_input.pack(side=LEFT, ipady=8)
password_input.bind("<FocusIn>", lambda e: password_input.config(highlightbackground=PRIMARY_COLOR))
password_input.bind("<FocusOut>", lambda e: password_input.config(highlightbackground="#cbd5e1"))

# Password toggle button
def toggle_password():
    if password_input.cget('show') == '•':
        password_input.config(show='')
        toggle_btn.config(text="👁", fg=TEXT_COLOR)
    else:
        password_input.config(show='•')
        toggle_btn.config(text="👁", fg="#64748b")

toggle_btn = Button(password_input_container, text="👁", font=("Helvetica", 12), 
                    bg=ENTRY_BG, fg="#64748b", bd=0, cursor="hand2",
                    activebackground=ENTRY_BG, command=toggle_password)
toggle_btn.pack(side=RIGHT, padx=(5, 0))

# Options Frame
options_frame = Frame(input_frame, bg=BG_COLOR)
options_frame.pack(fill="x", pady=(5, 20))

# Remember Me
remember_var = IntVar()
remember_check = Checkbutton(options_frame, text="Remember me", 
                            variable=remember_var, bg=BG_COLOR, fg=TEXT_COLOR, 
                            font=("Helvetica", 10), selectcolor=ACCENT_COLOR,
                            activebackground=BG_COLOR, cursor="hand2")
remember_check.pack(side=LEFT)

# Forgot Password
def on_forgot_password():
    messagebox.showinfo("Forgot Password", 
                       "Please contact your administrator\nor check your email for password reset instructions.")

forgot_btn = Button(options_frame, text="Forgot password?", 
                    font=("Helvetica", 10), bg=BG_COLOR, fg=PRIMARY_COLOR, 
                    bd=0, cursor="hand2", activebackground=BG_COLOR,
                    activeforeground=SECONDARY_COLOR, command=on_forgot_password)
forgot_btn.pack(side=RIGHT)

# Login Button
def validate_login():
    email = email_input.get().strip()
    password = password_input.get().strip()
    
    # Reset error states
    email_input.config(highlightbackground="#cbd5e1")
    password_input.config(highlightbackground="#cbd5e1")
    
    errors = []
    
    # Email validation
    if email == "" or email == "you@example.com":
        errors.append("Please enter your email address")
        email_input.config(highlightbackground=ERROR_COLOR)
    elif not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
        errors.append("Please enter a valid email address")
        email_input.config(highlightbackground=ERROR_COLOR)
    
    # Password validation
    if password == "":
        errors.append("Please enter your password")
        password_input.config(highlightbackground=ERROR_COLOR)
    elif len(password) < 6:
        errors.append("Password must be at least 6 characters")
        password_input.config(highlightbackground=ERROR_COLOR)
    
    if errors:
        messagebox.showerror("Login Failed", "\n".join(errors))
    else:
        # Simulate login process
        login_button.config(text="Authenticating...", state=DISABLED)
        root.after(1000, lambda: login_success(email))

def login_success(email):
    messagebox.showinfo("Login Successful", f"Welcome back, {email.split('@')[0]}!")
    login_button.config(text="Login", state=NORMAL)
    # Here you would typically navigate to the main application

# Login button with hover effect
def on_enter(e):
    login_button.config(bg=SECONDARY_COLOR)

def on_leave(e):
    login_button.config(bg=PRIMARY_COLOR)

login_button = Button(frame, text="Login", font=("Helvetica", 12, "bold"), 
                      bg=PRIMARY_COLOR, fg="#ffffff", width=28, 
                      cursor="hand2", relief="flat", bd=0,
                      activebackground=SECONDARY_COLOR, command=validate_login)
login_button.pack(pady=(10, 20), ipady=12)
login_button.bind("<Enter>", on_enter)
login_button.bind("<Leave>", on_leave)

# Divider
divider = Frame(frame, height=1, bg="#e2e8f0")
divider.pack(fill="x", pady=(0, 20), padx=20)

# Footer
footer_frame = Frame(frame, bg=BG_COLOR)
footer_frame.pack()

footer_label = Label(footer_frame, text="Don't have an account? ", 
                     font=("Helvetica", 10), fg="#64748b", bg=BG_COLOR)
footer_label.pack(side=LEFT)

def on_signup():
    messagebox.showinfo("Sign Up", "Please contact your administrator to create an account.")

signup_btn = Button(footer_frame, text="Sign up", 
                    font=("Helvetica", 10, "underline"), bg=BG_COLOR, 
                    fg=PRIMARY_COLOR, bd=0, cursor="hand2",
                    activebackground=BG_COLOR, activeforeground=SECONDARY_COLOR,
                    command=on_signup)
signup_btn.pack(side=LEFT)

# Add Enter key binding
def on_enter_key(event):
    validate_login()

root.bind('<Return>', on_enter_key)

# Center window on screen
root.update_idletasks()
width = root.winfo_width()
height = root.winfo_height()
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry(f'{width}x{height}+{x}+{y}')

root.mainloop()