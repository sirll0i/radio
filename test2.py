import tkinter as tk
from tkinter import messagebox
import mysql.connector
import re
import smtplib
from email.mime.text import MIMEText
import random
import string
import datetime
import winsound
import numpy as np
import math
import sqlite3

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.style as mplstyle
import customtkinter as ctk

# Appearance Setup
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")
mplstyle.use('fast')

def connect_db():
    try:
        return mysql.connector.connect(
            host="localhost", user="root", password="", port=3307, database="rf_db"
        )
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")
        return None

def send_email(receiver_email, message_body, subject="Password Reset"):
    sender_email = "qhrislora2004@gmail.com"
    app_password = "hhki lypz fclg holq" 
    msg = MIMEText(message_body)
    msg["Subject"], msg["From"], msg["To"] = subject, sender_email, receiver_email
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, app_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        return True
    except: return False

class RadioSimulatorApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Radio Frequency Simulator")
        self.geometry("1100x800")
        self.logged_user_name = ""

        # Simulation Variables
        self.freq_val = 50
        self.power_val = -20
        self.save_timer = None
        
        # Change Trackers (Prevents saving on login/static load)
        self.last_saved_freq = None
        self.last_saved_power = None

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.sidebar_frame = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        
        self.content_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="#f0f0f0") 
        self.content_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

        self.btn_objects = {}
        menus = [("Home", "home"), ("Radio", "radio"), ("Reports", "reports"), ("Settings", "settings"), ("About Us", "about")]
        for i, (text, d_id) in enumerate(menus):
            btn = ctk.CTkButton(self.sidebar_frame, text=text, fg_color="transparent", 
                                text_color=("gray10", "gray90"), anchor="w", command=lambda d=d_id: self.show_dashboard(d))
            btn.grid(row=i, column=0, padx=20, pady=10, sticky="ew")
            self.btn_objects[d_id] = btn

        self.logout_btn = ctk.CTkButton(self.sidebar_frame, text="Logout", fg_color="#c0392b", command=self.logout)
        self.logout_btn.grid(row=10, column=0, padx=20, pady=20, sticky="s")
        self.status_label = ctk.CTkLabel(self.sidebar_frame, text="", text_color="gray")
        self.status_label.grid(row=11, column=0, pady=10)

        self.withdraw() 
        self.show_login()

    # ================= 📊 DATA FETCHING =================
    def fetch_home_data(self):
        conn = connect_db()
        data = {'days': [], 'avg_freqs': [], 'status_counts': [0, 0, 0]}
        if not conn: return data
        try:
            cursor = conn.cursor()
            # 1. Trend Data
            cursor.execute("SELECT DATE_FORMAT(timestamp, '%b %d'), AVG(frequency) FROM frequency_logs GROUP BY DATE(timestamp) ORDER BY timestamp ASC LIMIT 7")
            for r in cursor.fetchall():
                data['days'].append(r[0]); data['avg_freqs'].append(float(r[1]))
            # 2. Status Distribution
            cursor.execute("SELECT SUM(CASE WHEN frequency >= 600 THEN 1 ELSE 0 END), SUM(CASE WHEN frequency >= 200 AND frequency < 600 THEN 1 ELSE 0 END), SUM(CASE WHEN frequency < 200 THEN 1 ELSE 0 END) FROM frequency_logs")
            res = cursor.fetchone()
            if res and res[0] is not None: data['status_counts'] = [int(x) for x in res]
        except: pass
        finally: conn.close()
        return data

    def show_dashboard(self, selection):
        for widget in self.content_frame.winfo_children(): widget.destroy()
        for d_id, btn in self.btn_objects.items(): btn.configure(fg_color="transparent")
        if selection in self.btn_objects: self.btn_objects[selection].configure(fg_color=("gray70", "gray30"))

        if selection == "home":
            # 1. Main Background and Scrollable Container
            home_container = ctk.CTkFrame(self.content_frame, fg_color="#f8f9fa") # Light professional gray
            home_container.pack(fill="both", expand=True)
            
            home_scroll = ctk.CTkScrollableFrame(home_container, fg_color="transparent")
            home_scroll.pack(fill="both", expand=True, padx=20, pady=10)

            # 2. Header Section
            header_frame = ctk.CTkFrame(home_scroll, fg_color="transparent")
            header_frame.pack(fill="x", pady=(10, 20))
            
            ctk.CTkLabel(header_frame, text="Network Performance Dashboard", 
                         font=("Helvetica", 28, "bold"), text_color="#2c3e50").pack(side="left")
            
            # 3. Fetch Real-time Data
            db_data = self.fetch_home_data()
            avg_freq = int(np.mean(db_data['avg_freqs'])) if db_data['avg_freqs'] else 0
            total_logs = sum(db_data['status_counts'])
            
            # 4. Quick Metrics Row (Top Cards)
            metrics_row = ctk.CTkFrame(home_scroll, fg_color="transparent")
            metrics_row.pack(fill="x", pady=10)
            
            def create_metric_card(parent, title, value, color):
                card = ctk.CTkFrame(parent, fg_color="white", corner_radius=12, border_width=1, border_color="#e0e0e0")
                card.pack(side="left", expand=True, fill="both", padx=10)
                ctk.CTkLabel(card, text=title, font=("Helvetica", 12), text_color="gray").pack(pady=(10, 0))
                ctk.CTkLabel(card, text=value, font=("Helvetica", 24, "bold"), text_color=color).pack(pady=(0, 10))

            create_metric_card(metrics_row, "Average Frequency", f"{avg_freq} MHz", "#2980b9")
            create_metric_card(metrics_row, "Total Data Logs", str(total_logs), "#2c3e50")
            status_text = "Healthy" if avg_freq > 200 else "Critical"
            create_metric_card(metrics_row, "System Status", status_text, "#27ae60" if status_text == "Healthy" else "#e74c3c")

            # 5. Frequency Trend Card (Line Chart)
            trend_card = ctk.CTkFrame(home_scroll, fg_color="white", corner_radius=15, border_width=1, border_color="#e0e0e0")
            trend_card.pack(fill="x", pady=15, padx=10)
            
            ctk.CTkLabel(trend_card, text="Frequency Trend (Last 7 Days)", font=("Helvetica", 16, "bold"), text_color="#34495e").pack(pady=10, padx=20, anchor="w")

            fig_t = Figure(figsize=(8, 3), dpi=100, facecolor="white")
            ax1 = fig_t.add_subplot(111)
            ax1.set_facecolor("#ffffff")
            # Aesthetic Zone Backgrounds
            ax1.axhspan(0, 200, color='#ff7675', alpha=0.1)  # Red zone
            ax1.axhspan(200, 600, color='#ffeaa7', alpha=0.1) # Yellow zone
            ax1.axhspan(600, 1000, color='#55efc4', alpha=0.1) # Green zone
            
            # Clean Line Plot
            ax1.plot(db_data['days'], db_data['avg_freqs'], marker='o', color='#0984e3', 
                     linewidth=3, markersize=8, markerfacecolor='white', markeredgewidth=2)
            
            ax1.spines['top'].set_visible(False)
            ax1.spines['right'].set_visible(False)
            ax1.tick_params(axis='both', which='major', labelsize=9, colors='#636e72')
            
            FigureCanvasTkAgg(fig_t, master=trend_card).get_tk_widget().pack(pady=10, padx=20, fill="x")

            # 6. Bottom Row: Status Distribution & Details
            bottom_row = ctk.CTkFrame(home_scroll, fg_color="transparent")
            bottom_row.pack(fill="x", pady=10)

            # Doughnut Chart Card
            pie_card = ctk.CTkFrame(bottom_row, fg_color="white", corner_radius=15, border_width=1, border_color="#e0e0e0")
            pie_card.pack(side="left", expand=True, fill="both", padx=10)

            ctk.CTkLabel(pie_card, text="Status Distribution", font=("Helvetica", 16, "bold"), text_color="#34495e").pack(pady=10)

            fig_p = Figure(figsize=(4, 4), dpi=100, facecolor="white")
            ax2 = fig_p.add_subplot(111)
            counts = db_data['status_counts']
            if sum(counts) > 0:
                wedges, _ = ax2.pie(counts, colors=['#00b894', '#fdcb6e', '#d63031'], 
                                    startangle=90, wedgeprops={'width': 0.4, 'edgecolor': 'white'})
                
                # Center Text (Uptime Percentage)
                uptime = (counts[0]/sum(counts)*100) if sum(counts)>0 else 0
                ax2.text(0, 0, f"{int(uptime)}%\nUptime", ha='center', va='center', 
                         fontweight='bold', fontsize=12, color='#2d3436')
            else:
                ax2.text(0.5, 0.5, "No Data", ha='center', va='center')
            
            FigureCanvasTkAgg(fig_p, master=pie_card).get_tk_widget().pack(pady=5)

            # Legend/Detail Card
            detail_card = ctk.CTkFrame(bottom_row, fg_color="white", corner_radius=15, border_width=1, border_color="#e0e0e0")
            detail_card.pack(side="left", expand=True, fill="both", padx=10)
            
            ctk.CTkLabel(detail_card, text="Operational Legend", font=("Helvetica", 16, "bold"), text_color="#34495e").pack(pady=10)
            
            def create_legend_item(text, color):
                item = ctk.CTkFrame(detail_card, fg_color="transparent")
                item.pack(fill="x", padx=30, pady=5)
                ctk.CTkFrame(item, width=15, height=15, fg_color=color, corner_radius=4).pack(side="left")
                ctk.CTkLabel(item, text=text, font=("Helvetica", 13), text_color="#636e72").pack(side="left", padx=10)

            create_legend_item("Stable (> 600 MHz)", "#00b894")
            create_legend_item("Caution (200-600 MHz)", "#fdcb6e")
            create_legend_item("Critical (< 200 MHz)", "#d63031")

        elif selection == "radio": self.load_radio_sim()
        elif selection == "settings": self.load_settings()
        elif selection == "reports": self.show_reports_dashboard()
        elif selection == "about":
            # 1. Main Container
            about_container = ctk.CTkFrame(self.content_frame, fg_color="white", corner_radius=15)
            about_container.pack(pady=40, padx=40, fill="both", expand=True)

            # 2. Header
            ctk.CTkLabel(about_container, text="About the Project", 
                         font=("Helvetica", 28, "bold"), text_color="#2c3e50").pack(pady=(30, 10))
            
            ctk.CTkLabel(about_container, text="This Radio Frequency Simulator is a specialized diagnostic tool \ndesigned for network performance sample testing.", 
                         font=("Helvetica", 14), text_color="#7f8c8d", justify="center").pack(pady=10)

            # 3. Separator Line
            ctk.CTkFrame(about_container, height=2, fg_color="#ecf0f1").pack(fill="x", padx=100, pady=20)

            # 4. Developers Section
            ctk.CTkLabel(about_container, text="DEVELOPMENT TEAM", 
                         font=("Helvetica", 12, "bold"), text_color="#3498db").pack(pady=(10, 20))

            # Team Card Frame
            team_frame = ctk.CTkFrame(about_container, fg_color="transparent")
            team_frame.pack(pady=10)

            def create_member_card(parent, name, role):
                card = ctk.CTkFrame(parent, fg_color="#f8f9fa", corner_radius=10, border_width=1, border_color="#e0e0e0", width=300)
                card.pack(pady=5, fill="x")
                ctk.CTkLabel(card, text=name, font=("Helvetica", 16, "bold"), text_color="#2c3e50").pack(pady=(10, 0), padx=20)
                ctk.CTkLabel(card, text=role, font=("Helvetica", 12), text_color="#2980b9").pack(pady=(0, 10), padx=20)

            # Adding Team Members
            create_member_card(team_frame, "Group 1", "Core Development Unit")
            create_member_card(team_frame, "Loy Floro", "Main Developer")
            create_member_card(team_frame, "Qhris", "Frontend & Backend Developer")

            # 5. Footer / Version
            ctk.CTkLabel(about_container, text="Version 1.0.4 | © 2026 RadioSim", 
                         font=("Helvetica", 10), text_color="gray").pack(side="bottom", pady=20)
        else: ctk.CTkLabel(self.content_frame, text=f"{selection.title()} View", font=("Arial", 24), text_color="black").pack(pady=20)

    # ================= 📡 RADIO SIMULATOR =================
    def load_radio_sim(self):
        # State variables
        self.is_auto = False
        self.auto_direction = 1
        self.save_timer = None
        self.is_muted = False
        self.last_saved_freq = self.freq_val
        self.last_saved_power = self.power_val

        # Main Background Container
        radio_bg = ctk.CTkFrame(self.content_frame, fg_color="#1e272e", corner_radius=20, border_width=2, border_color="#34495e")
        radio_bg.pack(fill="both", expand=True, padx=20, pady=20)

        # --- Top Section: Display ---
        self.radio_screen = ctk.CTkFrame(radio_bg, fg_color="black", corner_radius=10, border_width=2, border_color="#34495e")
        self.radio_screen.pack(fill="both", expand=True, padx=30, pady=(20, 10))

        self.fig = Figure(figsize=(7, 2), dpi=100)
        self.ax = self.fig.add_subplot(111); self.ax.set_facecolor("black")
        self.ax.tick_params(colors='#00FF00', labelsize=8)
        self.x_vals = list(range(50, 1001, 10))
        self.line, = self.ax.plot(self.x_vals, [0]*len(self.x_vals), color='#00FF00', linewidth=1.5)
        self.canvas_plot = FigureCanvasTkAgg(self.fig, master=self.radio_screen)
        self.canvas_plot.get_tk_widget().pack(pady=10, fill="both", expand=True)

        self.freq_display = ctk.CTkLabel(radio_bg, text="50 MHz", font=("Consolas", 50, "bold"), text_color="#F1C40F")
        self.freq_display.pack(pady=5)

        # --- Middle Section: CIRCULAR LIGHTS ---
        light_frame = ctk.CTkFrame(radio_bg, fg_color="transparent")
        light_frame.pack(pady=10)

        self.canvases = []
        self.circles = []
        labels = ["LOW BAND", "MID BAND", "HIGH BAND"]

        for i in range(3):
            container = ctk.CTkFrame(light_frame, fg_color="transparent")
            container.pack(side="left", padx=25)
            
            canv = tk.Canvas(container, width=40, height=40, bg="#1e272e", highlightthickness=0)
            canv.pack()
            circ = canv.create_oval(5, 5, 35, 35, fill="grey")
            
            self.canvases.append(canv)
            self.circles.append(circ)
            ctk.CTkLabel(container, text=labels[i], font=("Arial", 9, "bold"), text_color="#95a5a6").pack()

        # --- Bottom Section: Control Panel ---
        ctrl_panel = ctk.CTkFrame(radio_bg, fg_color="#2f3542", corner_radius=15)
        ctrl_panel.pack(fill="x", padx=30, pady=(10, 20))

        # Manual/Auto Switch
        self.mode_switch = ctk.CTkSegmentedButton(ctrl_panel, values=["MANUAL", "AUTO"], 
                                                 command=self.toggle_mode, selected_color="#3498db")
        self.mode_switch.set("MANUAL")
        self.mode_switch.pack(pady=10)

        slider_grid = ctk.CTkFrame(ctrl_panel, fg_color="transparent")
        slider_grid.pack(fill="x", padx=20, pady=10)

        # Frequency Slider Group
        f_group = ctk.CTkFrame(slider_grid, fg_color="transparent")
        f_group.pack(side="left", expand=True)
        ctk.CTkLabel(f_group, text="FREQUENCY", font=("Arial", 10, "bold")).pack()
        self.f_knob = ctk.CTkSlider(f_group, from_=50, to=1000, width=250, command=self.update_freq)
        self.f_knob.pack(pady=5)

        # Power Slider Group
        p_group = ctk.CTkFrame(slider_grid, fg_color="transparent")
        p_group.pack(side="right", expand=True)
        ctk.CTkLabel(p_group, text="POWER", font=("Arial", 10, "bold")).pack()
        self.p_knob = ctk.CTkSlider(p_group, from_=-50, to=10, width=250, command=self.update_power)
        self.p_knob.pack(pady=5)

        self.update_radio_logic(is_init=True)

    def toggle_mute(self):
        self.is_muted = not self.mute_btn.get()

    def toggle_mode(self, mode):
        if mode == "AUTO":
            self.is_auto = True
            self.f_knob.configure(state="disabled")
            self.run_auto_scan()
        else:
            self.is_auto = False
            self.f_knob.configure(state="normal")

    def play_beep(self):
        """Plays beep in a separate thread. Ensure system volume is up!"""
        if not self.is_muted:
            try:
                # Frequency: 600Hz, Duration: 200ms
                # This is a standard 'alert' tone
                winsound.Beep(600, 200)
            except Exception as e:
                print(f"Beep error: {e}")

    def toggle_mode(self, mode):
        if mode == "AUTO":
            self.is_auto = True
            self.f_knob.configure(state="disabled")
            self.run_auto_scan()
        else:
            self.is_auto = False
            self.f_knob.configure(state="normal")

    def run_auto_scan(self):
        if not self.is_auto: return
        current_f = self.f_knob.get()
        if current_f >= 1000: self.auto_direction = -1
        if current_f <= 50: self.auto_direction = 1
        new_f = current_f + (5 * self.auto_direction)
        self.f_knob.set(new_f)
        self.update_freq(new_f)
        self.after(100, self.run_auto_scan)

    def update_freq(self, val):
        self.freq_val = int(float(val))
        self.update_radio_logic()

    def update_power(self, val):
        self.power_val = int(float(val))
        self.update_radio_logic()

    def save_frequency_log(self):
        if self.freq_val == self.last_saved_freq and self.power_val == self.last_saved_power:
            return
        conn = connect_db()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO frequency_logs (username, frequency, power_level) VALUES (%s, %s, %s)",
                               (self.logged_user_name, self.freq_val, self.power_val))
                conn.commit()
                self.last_saved_freq = self.freq_val
                self.last_saved_power = self.power_val
                print(f"Logged Change: {self.freq_val} MHz")
            except Exception as e: print(e)
            finally: conn.close()

    def update_radio_logic(self, is_init=False):
        self.freq_display.configure(text=f"{self.freq_val} MHz")
        
        # Update Plot with Power level effect
        y = [random.randint(-10, 10) + (self.power_val) for _ in self.x_vals]
        peak_idx = int((self.freq_val - 50) / 10)
        if 0 <= peak_idx < len(y): y[peak_idx] += 30 
        self.line.set_ydata(y); self.ax.set_ylim(-60, 50); self.canvas_plot.draw()

        # Reset circles
        for i in range(3):
            self.canvases[i].itemconfig(self.circles[i], fill="grey")

        # Band Logic + Beeping
        if self.freq_val < 350:
            self.canvases[0].itemconfig(self.circles[0], fill="red")
            if not is_init:
                winsound.Beep(1000, 100) # Fast beep like your test script
        elif self.freq_val <= 700:
            self.canvases[1].itemconfig(self.circles[1], fill="yellow")
        else:
            self.canvases[2].itemconfig(self.circles[2], fill="green")

        if not is_init:
            if self.save_timer: self.after_cancel(self.save_timer)
            self.save_timer = self.after(3000, self.save_frequency_log)

    # ================= ⚙️ USER SETTINGS (MANAGEMENT) =================
    def load_settings(self):
        form_frame = ctk.CTkFrame(self.content_frame, fg_color="white", corner_radius=15)
        form_frame.pack(pady=30, padx=30, fill="both", expand=True)

        ctk.CTkLabel(form_frame, text="User Account Management", 
                     font=("Arial", 24, "bold"), text_color="#2c3e50").pack(pady=20)

        input_container = ctk.CTkFrame(form_frame, fg_color="transparent")
        input_container.pack(pady=10)

        fields = ["Username", "Password", "Name", "Email"]
        self.entries = {}

        for field in fields:
            row = ctk.CTkFrame(input_container, fg_color="transparent")
            row.pack(fill="x", pady=5)
            
            ctk.CTkLabel(row, text=field, width=100, anchor="w", text_color="black").pack(side="left")
            entry = ctk.CTkEntry(row, width=250, show="*" if field == "Password" else "", 
                                 fg_color="#ecf0f1", text_color="black")
            entry.pack(side="left", padx=10)
            self.entries[field.lower()] = entry

        def validate():
            if any(not e.get() for e in self.entries.values()):
                messagebox.showerror("Error", "Please fill up all details!")
                return False
            if not re.match(r"[^@]+@[^@]+\.[^@]+", self.entries['email'].get()):
                messagebox.showerror("Error", "Invalid email format!")
                return False
            return True

        def clear_fields():
            for e in self.entries.values(): e.delete(0, tk.END)

        def save_user():
            if not validate(): return
            conn = connect_db()
            if not conn: return
            cursor = conn.cursor()
            try:
                cursor.execute(
                    "INSERT INTO user (username, password, name, email) VALUES (%s,%s,%s,%s)",
                    (self.entries['username'].get(), self.entries['password'].get(), 
                     self.entries['name'].get(), self.entries['email'].get())
                )
                conn.commit()
                messagebox.showinfo("Success", "User successfully saved!")
                clear_fields()
            except mysql.connector.IntegrityError:
                messagebox.showerror("Error", "Username already exists!")
            finally: conn.close()

        def search_user():
            u = self.entries['username'].get()
            if not u:
                messagebox.showerror("Error", "Enter a username to search!")
                return
            conn = connect_db()
            if not conn: return
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM user WHERE username=%s", (u,))
            res = cursor.fetchone()
            conn.close()
            if res:
                clear_fields()
                self.entries['username'].insert(0, res[1])
                self.entries['password'].insert(0, res[2])
                self.entries['name'].insert(0, res[3])
                self.entries['email'].insert(0, res[4])
            else:
                messagebox.showerror("Error", "User not found!")

        def update_user():
            if not validate(): return
            conn = connect_db()
            if not conn: return
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE user SET password=%s, name=%s, email=%s WHERE username=%s",
                (self.entries['password'].get(), self.entries['name'].get(), 
                 self.entries['email'].get(), self.entries['username'].get())
            )
            conn.commit()
            if cursor.rowcount > 0:
                messagebox.showinfo("Success", "User details updated!")
                clear_fields()
            else:
                messagebox.showerror("Error", "Update failed. User not found.")
            conn.close()

        def delete_user():
            u = self.entries['username'].get()
            if not u:
                messagebox.showerror("Error", "Enter username to delete!")
                return
            if messagebox.askyesno("Confirm", f"Are you sure you want to delete {u}?"):
                conn = connect_db()
                if not conn: return
                cursor = conn.cursor()
                cursor.execute("DELETE FROM user WHERE username=%s", (u,))
                conn.commit()
                if cursor.rowcount > 0:
                    messagebox.showinfo("Deleted", "User has been removed.")
                    clear_fields()
                else:
                    messagebox.showerror("Error", "User not found.")
                conn.close()

        btn_row = ctk.CTkFrame(form_frame, fg_color="transparent")
        btn_row.pack(pady=30)
        ctk.CTkButton(btn_row, text="Search", width=90, fg_color="#34495e", command=search_user).pack(side="left", padx=5)
        ctk.CTkButton(btn_row, text="Save", width=90, fg_color="#27ae60", command=save_user).pack(side="left", padx=5)
        ctk.CTkButton(btn_row, text="Update", width=90, fg_color="#2980b9", command=update_user).pack(side="left", padx=5)
        ctk.CTkButton(btn_row, text="Delete", width=90, fg_color="#c0392b", command=delete_user).pack(side="left", padx=5)
        ctk.CTkButton(btn_row, text="Clear", width=90, fg_color="gray", command=clear_fields).pack(side="left", padx=5)

# ================= 📊 DYNAMIC REPORTS =================
    def show_reports_dashboard(self):
        # Clear previous content
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        # --- Header & Toggle ---
        header_frame = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        header_frame.pack(fill="x", padx=20, pady=20)
        
        ctk.CTkLabel(header_frame, text="System Reports", font=("Arial", 24, "bold"), text_color="black").pack(side="left")
        
        # Toggle switch for History vs Logs
        self.report_type = ctk.CTkSegmentedButton(header_frame, values=["Frequency History", "System Logs"],
                                                 command=self.refresh_report_table)
        self.report_type.set("Frequency History")
        self.report_type.pack(side="right")

        # --- Table Container ---
        self.report_container = ctk.CTkScrollableFrame(self.content_frame, fg_color="#2f3542", corner_radius=15)
        self.report_container.pack(fill="both", expand=True, padx=20, pady=(0, 20))

        # Initial Load
        self.refresh_report_table("Frequency History")

    def refresh_report_table(self, view_type):
        # Clear existing table rows
        for widget in self.report_container.winfo_children():
            widget.destroy()

        conn = connect_db()
        if not conn:
            return

        cursor = conn.cursor()
        data = []
        headers = []

        try:
            if view_type == "Frequency History":
                headers = ["DATE AND TIME", "FREQUENCY", "RANGE", "MODE", "USER"]
                # Query logic: determine Range based on frequency value
                query = """
                    SELECT timestamp, frequency, 
                    CASE 
                        WHEN frequency < 350 THEN 'LOW' 
                        WHEN frequency <= 700 THEN 'MEDIUM' 
                        ELSE 'HIGH' 
                    END as f_range, 
                    'Manual' as mode, username 
                    FROM frequency_logs 
                    ORDER BY timestamp DESC
                """
                cursor.execute(query)
            else:
                # You may need to create an 'activity_logs' table in your MySQL if you haven't yet
                headers = ["USER", "ACTION", "DATE AND TIME"]
                cursor.execute("SELECT username, 'Adjusted Settings', timestamp FROM frequency_logs ORDER BY timestamp DESC")
            
            data = cursor.fetchall()
        except Exception as e:
            print(f"Fetch error: {e}")
        finally:
            conn.close()

        # Render Headers
        for col, text in enumerate(headers):
            header_cell = ctk.CTkFrame(self.report_container, fg_color="#1e272e", corner_radius=0, border_width=1)
            header_cell.grid(row=0, column=col, sticky="nsew")
            ctk.CTkLabel(header_cell, text=text, font=("Arial", 12, "bold"), text_color="white", width=160).pack(pady=10, padx=5)

        # Render Data Rows
        if not data:
            ctk.CTkLabel(self.report_container, text="No records found in database.", text_color="gray").grid(row=1, column=0, columnspan=len(headers), pady=20)
        else:
            for row_idx, row_data in enumerate(data, start=1):
                for col_idx, value in enumerate(row_data):
                    # Alternating row colors
                    bg = "#3d4451" if row_idx % 2 == 0 else "#2f3542"
                    cell = ctk.CTkFrame(self.report_container, fg_color=bg, corner_radius=0, border_width=1, border_color="#57606f")
                    cell.grid(row=row_idx, column=col_idx, sticky="nsew")
                    
                    # Formating timestamp or frequency to string
                    text_val = str(value)
                    ctk.CTkLabel(cell, text=text_val, font=("Arial", 11), text_color="white").pack(pady=8, padx=5)

    # ================= 🔐 LOGIN & LOGOUT =================
    def show_forgot_password(self):
        win = ctk.CTkToplevel(self.login_win)
        win.geometry("350x250")
        win.title("Reset")
        win.attributes("-topmost", True)
        ctk.CTkLabel(win, text="Username:").pack(pady=10)
        f_user = ctk.CTkEntry(win, width=200)
        f_user.pack(pady=5)

        def do_reset():
            conn = connect_db()
            if not conn: return
            cursor = conn.cursor()
            cursor.execute("SELECT email FROM user WHERE username=%s", (f_user.get(),))
            res = cursor.fetchone()
            if res:
                new_p = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
                if send_email(res[0], f"New Password: {new_p}"):
                    cursor.execute("UPDATE user SET password=%s WHERE username=%s", (new_p, f_user.get()))
                    conn.commit()
                    messagebox.showinfo("Done", "Password sent to email")
                    win.destroy()
            else: messagebox.showerror("Fail", "User not found")
            conn.close()

        ctk.CTkButton(win, text="Reset via Email", command=do_reset).pack(pady=20)

    def show_login(self):
        self.login_win = ctk.CTkToplevel()
        self.login_win.geometry("400x500")
        self.login_win.protocol("WM_DELETE_WINDOW", self.destroy)
        ctk.CTkLabel(self.login_win, text="RF LOGIN", font=("Arial", 24, "bold")).pack(pady=50)
        u_e = ctk.CTkEntry(self.login_win, placeholder_text="Username", width=250)
        u_e.pack(pady=10)
        p_e = ctk.CTkEntry(self.login_win, placeholder_text="Password", show="*", width=250)
        p_e.pack(pady=10)

        def login():
            conn = connect_db()
            if conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM user WHERE username=%s AND password=%s", (u_e.get(), p_e.get()))
                if cursor.fetchone():
                    self.logged_user_name = u_e.get()
                    self.login_win.destroy()
                    self.deiconify()
                    self.show_dashboard("home")
                    self.update_status()
                else: messagebox.showerror("Error", "Invalid login")
                conn.close()

        ctk.CTkButton(self.login_win, text="Login", width=250, command=login).pack(pady=20)
        ctk.CTkButton(self.login_win, text="Forgot Password?", fg_color="transparent", command=self.show_forgot_password).pack()

    def logout(self):
        if messagebox.askyesno("Exit", "Logout?"):
            self.withdraw()
            self.show_login()

    def update_status(self):
        now = datetime.datetime.now().strftime("%I:%M %p")
        self.status_label.configure(text=f"User: {self.logged_user_name}\n{now}")
        self.after(1000, self.update_status)

if __name__ == "__main__":
    app = RadioSimulatorApp()
    app.mainloop()
