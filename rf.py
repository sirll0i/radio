import tkinter as tk
from tkinter import messagebox
import mysql.connector
import re
import smtplib
from email.mime.text import MIMEText
import random
import string

# ================= DATABASE CONNECTION =================
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",         # your MySQL root password
        database="rf_db"     # your database name
    )

# ================= EMAIL FUNCTION =================
def send_email(to_email, new_password):
    sender_email = "yourgmail@gmail.com"        # REPLACE with your Gmail
    sender_password = "your_app_password"       # REPLACE with 16-char App Password

    msg = MIMEText(f"Your new password is: {new_password}")
    msg["Subject"] = "Password Reset"
    msg["From"] = sender_email
    msg["To"] = to_email

    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()
        return True
    except Exception as e:
        print("Email sending error:", e)
        return False

# ================= LOGIN FUNCTION =================
def login():
    username = entry_user.get().strip()
    password = entry_pass.get().strip()

    if username == "" or password == "":
        messagebox.showerror("Error", "Enter Username and Password")
        return

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user WHERE username=%s AND password=%s", (username, password))
    result = cursor.fetchone()
    conn.close()

    if result:
        messagebox.showinfo("Success", "Login Successful!")
        root.destroy()
        open_main_form()
    else:
        messagebox.showerror("Error", "Invalid Username or Password")
        entry_pass.delete(0, tk.END)
        entry_user.focus()

# ================= FORGOT PASSWORD =================
def forgot_password():
    def reset():
        user = entry_fuser.get().strip()

        if user == "":
            messagebox.showerror("Error", "Enter username!")
            return

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT email FROM user WHERE username=%s", (user,))
        result = cursor.fetchone()

        if not result:
            messagebox.showerror("Error", "Username not found")
            conn.close()
            return

        email = result[0]

        # GENERATE RANDOM PASSWORD
        new_password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))

        # SEND EMAIL
        if send_email(email, new_password):
            cursor.execute("UPDATE user SET password=%s WHERE username=%s", (new_password, user))
            conn.commit()
            messagebox.showinfo("Success", f"New password sent to {email}")
            forgot_win.destroy()
        else:
            messagebox.showerror("Error", "Failed to send email. Check Gmail App Password or internet connection.")
        conn.close()

    forgot_win = tk.Toplevel()
    forgot_win.title("Forgot Password")
    forgot_win.geometry("300x150")

    tk.Label(forgot_win, text="Enter Username").pack(pady=10)
    entry_fuser = tk.Entry(forgot_win)
    entry_fuser.pack()
    entry_fuser.focus()
    
    forgot_win.update_idletasks()  # Update "requested size" from geometry
    width = 300
    height = 150
    screen_width = forgot_win.winfo_screenwidth()
    screen_height = forgot_win.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    forgot_win.geometry(f"{width}x{height}+{x}+{y}")

    tk.Button(forgot_win, text="Reset Password", command=reset).pack(pady=10)

# ================= MAIN DASHBOARD =================
def open_main_form():
    main = tk.Tk()
    main.title("Dashboard")
    main.geometry("800x500")

    width = 800
    height = 500
    
    screen_width = main.winfo_screenwidth()
    screen_height = main.winfo_screenheight()
    
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    
    main.geometry(f"{width}x{height}+{x}+{y}")
    main.resizable(False, False)  # Optional: prevent resizing
    
    
    sidebar = tk.Frame(main, bg="#2c3e50", width=200)
    sidebar.pack(side="left", fill="y")

    content = tk.Frame(main, bg="white")
    content.pack(side="right", expand=True, fill="both")

    dashboard_var = tk.StringVar(value="home")

    def clear_content():
        for widget in content.winfo_children():
            widget.destroy()

    # ================= DASHBOARD VIEWS =================
    def show_dashboard(selection):
        clear_content()
        
        if selection == "home":
            tk.Label(content, text="Home Dashboard", font=("Arial", 20)).pack(pady=20)
            tk.Label(content, text="Dito ilalagay ang mga analytics", font=("Arial", 20)).pack(pady=50)
        elif selection == "radio":
            tk.Label(content, text="Radio Frequency Simulation Dashboard", font=("Arial", 20)).pack(pady=20)
            tk.Label(content, text="Dito ilalagay ang simulation", font=("Arial", 20)).pack(pady=50)
        elif selection == "reports":
            tk.Label(content, text="Reports Dashboard", font=("Arial", 20)).pack(pady=20)
            tk.Label(content, text="Dito ilalagay ang mga ", font=("Arial", 20)).pack(pady=50)
            tk.Label(content, text="report at history, lagyan ng table ", font=("Arial", 20)).pack(pady=20)
        
        elif selection == "settings":
            show_settings()   
        elif selection == "about":
            # ================= ABOUT US DASHBOARD =================
            tk.Label(content, text="About Us", font=("Arial", 20)).pack(pady=10)
            tk.Label(content, text="This Simulation is a sample test.", font=("Arial", 14)).pack(pady=5)
            tk.Label(content, text="Developed By:", font=("Arial", 14, "underline")).pack(pady=5)
            tk.Label(content, text="Group 1", font=("Arial", 12)).pack()
            tk.Label(content, text="Main Dev: Loy Floro", font=("Arial", 12)).pack()
            tk.Label(content, text="Frontend and Backend Dev: Qhris", font=("Arial", 12)).pack()

            
           
    # ================= USER SETTINGS =================
    def show_settings():
        clear_content()
        tk.Label(content, text="User Management", font=("Arial", 18)).grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(content, text="Username").grid(row=1, column=0)
        entry_username = tk.Entry(content)
        entry_username.grid(row=1, column=1)

        tk.Label(content, text="Password").grid(row=2, column=0)
        entry_password = tk.Entry(content, show="*")
        entry_password.grid(row=2, column=1)

        tk.Label(content, text="Name").grid(row=3, column=0)
        entry_name = tk.Entry(content)
        entry_name.grid(row=3, column=1)

        tk.Label(content, text="Email").grid(row=4, column=0)
        entry_email = tk.Entry(content)
        entry_email.grid(row=4, column=1)

        def clear_fields():
            entry_username.delete(0, tk.END)
            entry_password.delete(0, tk.END)
            entry_name.delete(0, tk.END)
            entry_email.delete(0, tk.END)

        def validate():
            if (entry_username.get()=="" or entry_password.get()=="" or entry_name.get()=="" or entry_email.get()==""):
                messagebox.showerror("Error", "Please fill up all details!")
                return False
            if not re.match(r"[^@]+@[^@]+\.[^@]+", entry_email.get()):
                messagebox.showerror("Error", "Invalid email format!")
                return False
            return True

        def save_user():
            if not validate():
                return
            conn = connect_db()
            cursor = conn.cursor()
            try:
                cursor.execute(
                    "INSERT INTO user (username, password, name, email) VALUES (%s,%s,%s,%s)",
                    (entry_username.get(), entry_password.get(), entry_name.get(), entry_email.get())
                )
                conn.commit()
                messagebox.showinfo("Success", "User Saved")
                clear_fields()
            except mysql.connector.IntegrityError:
                messagebox.showerror("Error", "Username already exists")
            conn.close()

        def search_user():
            if entry_username.get()=="":
                messagebox.showerror("Error", "Enter username!")
                return
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM user WHERE username=%s", (entry_username.get(),))
            result = cursor.fetchone()
            conn.close()
            if result:
                entry_password.delete(0, tk.END)
                entry_name.delete(0, tk.END)
                entry_email.delete(0, tk.END)
                entry_password.insert(0, result[2])
                entry_name.insert(0, result[3])
                entry_email.insert(0, result[4])
            else:
                messagebox.showerror("Error", "User not found")

        def update_user():
            if not validate():
                return
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE user SET password=%s,name=%s,email=%s WHERE username=%s",
                (entry_password.get(), entry_name.get(), entry_email.get(), entry_username.get())
            )
            conn.commit()
            if cursor.rowcount > 0:
                messagebox.showinfo("Success", "User Updated")
                clear_fields()
            else:
                messagebox.showerror("Error", "User not found")
            conn.close()

        def delete_user():
            if entry_username.get()=="":
                messagebox.showerror("Error", "Enter username!")
                return
            confirm = messagebox.askyesno("Confirm", "Delete this user?")
            if not confirm:
                return
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM user WHERE username=%s", (entry_username.get(),))
            conn.commit()
            if cursor.rowcount > 0:
                messagebox.showinfo("Success", "User Deleted")
                clear_fields()
            else:
                messagebox.showerror("Error", "User not found")
            conn.close()

        tk.Button(content, text="Save", width=12, command=save_user).grid(row=13, column=1)
        tk.Button(content, text="Search", width=12, command=search_user).grid(row=13, column=2)
        tk.Button(content, text="Update", width=12, command=update_user).grid(row=13, column=3)
        tk.Button(content, text="Delete", width=12, command=delete_user).grid(row=13, column=4)
        tk.Button(content, text="Clear", width=12, command=clear_fields).grid(row=13, column=6)

    # ================= LOGOUT =================
    def logout():
        confirm = messagebox.askyesno("Confirm Logout", "Do you want to exit the application?")
        if confirm:
            main.destroy()
            create_login_form()

    # ================= RADIO BUTTONS IN SIDEBAR =================
    tk.Label(sidebar, text="Dashboards", bg="#2c3e50", fg="white", font=("Arial", 12)).pack(pady=10)

    btn_home = tk.Button(sidebar, text="  Home", anchor="w", fg="white", bg="#34495e", width=20, command=lambda: show_dashboard("home"))
    btn_home.pack(pady=5)

    btn_radio = tk.Button(sidebar, text="  Radio", anchor="w", fg="white", bg="#34495e", width=20, command=lambda: show_dashboard("radio"))
    btn_radio.pack(pady=5)

    btn_reports = tk.Button(sidebar, text="  Reports", anchor="w", fg="white", bg="#34495e", width=20, command=lambda: show_dashboard("reports"))
    btn_reports.pack(pady=5)

    btn_settings = tk.Button(sidebar, text="  Settings", anchor="w", fg="white", bg="#34495e", width=20, command=lambda: show_dashboard("settings"))
    btn_settings.pack(pady=5)
    
    btn_about = tk.Button(sidebar, text="  About Us", anchor="w", fg="white", bg="#34495e", width=20, command=lambda: show_dashboard("about"))
    btn_about.pack(pady=5)

    #tk.Button(sidebar, text="  Logout", anchor="w", fg="white", bg="red", width=20, command=logout).pack(pady=10)
    tk.Button(sidebar, text="  Logout", anchor="w", fg="white", bg="red", width=20, command=logout)\
    .pack(side="bottom", fill="x", pady=10)
    
    show_dashboard()
    main.mainloop()

# ================= LOGIN FORM =================
def create_login_form():
    global root, entry_user, entry_pass

    root = tk.Tk()
    root.title("Login")

    # Window size
    width = 350
    height = 250

    # Get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate x and y coordinates to center the window
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)

    # Set geometry
    root.geometry(f"{width}x{height}+{x}+{y}")
    root.resizable(False, False)  # Optional: prevent resizing

    tk.Label(root, text="LOGIN", font=("Arial", 16)).pack(pady=10)

    tk.Label(root, text="Username").pack()
    entry_user = tk.Entry(root)
    entry_user.pack()
    entry_user.focus()

    tk.Label(root, text="Password").pack()
    entry_pass = tk.Entry(root, show="*")
    entry_pass.pack()


   # Frame to hold the buttons horizontally
    button_frame = tk.Frame(root)
    button_frame.pack(pady=20)

    # Login button
    tk.Button(button_frame, text="Login", width=12, command=login).pack(side="left", padx=5)

    # Forgot Password button
    tk.Button(button_frame, text="Forgot Password?", width=15, command=forgot_password).pack(side="left", padx=5)
   # tk.Button(root, text="Login", command=login).pack(pady=10)
    #tk.Button(root, text="Forgot Password?", command=forgot_password).pack()

    root.mainloop()

# ================= RUN =================
create_login_form()