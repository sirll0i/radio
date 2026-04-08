import tkinter as tk
import random
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import winsound  # For buzzer

# ================= MAIN APP =================
root = tk.Tk()
root.title("RF System Dashboard")
root.geometry("1000x600")  # Window size

# ================= SIDEBAR =================
sidebar = tk.Frame(root, width=200, bg="#2c3e50")
sidebar.pack(side="left", fill="y")

def show_dashboard(selection):
    clear_content()
    if selection == "home":
        tk.Label(content, text="Home Dashboard", font=("Arial", 20)).pack(pady=20)
    elif selection == "radio":
        show_radio_dashboard()

# Sidebar buttons
tk.Button(sidebar, text="Home", fg="white", bg="#34495e", command=lambda: show_dashboard("home")).pack(fill="x", pady=5)
tk.Button(sidebar, text="Radio Simulator", fg="white", bg="#34495e", command=lambda: show_dashboard("radio")).pack(fill="x", pady=5)

# ================= CONTENT AREA =================
content = tk.Frame(root, bg="#ecf0f1")
content.pack(side="left", fill="both", expand=True)

def clear_content():
    for widget in content.winfo_children():
        widget.destroy()

# ================= RADIO SIMULATOR DASHBOARD =================
def show_radio_dashboard():
    clear_content()
    
    simulator_frame = tk.Frame(content, bg="#bdc3c7", width=700, height=500)
    simulator_frame.place(relx=0.5, rely=0.5, anchor="center")  # Centered
    
    # Title
    tk.Label(simulator_frame, text="Radio Frequency Simulator", font=("Arial", 16, "bold"), bg="#bdc3c7").pack(pady=10)
    
    # ---------------- SIGNAL GENERATOR ----------------
    sg_frame = tk.LabelFrame(simulator_frame, text="Signal Generator", padx=10, pady=10, bg="#bdc3c7")
    sg_frame.pack(pady=10)
    
    tk.Label(sg_frame, text="Frequency (MHz):", bg="#bdc3c7").grid(row=0, column=0, sticky="w")
    freq_slider = tk.Scale(sg_frame, from_=50, to=1000, orient="horizontal", length=400)
    freq_slider.grid(row=0, column=1, padx=10)
    
    tk.Label(sg_frame, text="Power (dBm):", bg="#bdc3c7").grid(row=1, column=0, sticky="w")
    power_slider = tk.Scale(sg_frame, from_=-50, to=10, orient="horizontal", length=400)
    power_slider.grid(row=1, column=1, padx=10)
    
    # ---------------- SPECTRUM PLOT ----------------
    fig = Figure(figsize=(6,2), dpi=100)
    ax = fig.add_subplot(111)
    ax.set_title("Spectrum Analyzer")
    ax.set_xlabel("Frequency (MHz)")
    ax.set_ylabel("Amplitude (dBm)")
    
    x = list(range(50, 1001, 10))
    y = [random.randint(-50, 0) for _ in x]
    line, = ax.plot(x, y, color='green')
    
    canvas = FigureCanvasTkAgg(fig, master=simulator_frame)
    canvas.get_tk_widget().pack(pady=10)
    
    # ---------------- CIRCULAR LIGHT INDICATORS ----------------
    light_frame = tk.Frame(simulator_frame, bg="#bdc3c7")
    light_frame.pack(pady=10)
    
    canvas_red = tk.Canvas(light_frame, width=50, height=50, bg="#bdc3c7", highlightthickness=0)
    canvas_red.pack(side="left", padx=10)
    red_circle = canvas_red.create_oval(5,5,45,45, fill="grey")
    
    canvas_yellow = tk.Canvas(light_frame, width=50, height=50, bg="#bdc3c7", highlightthickness=0)
    canvas_yellow.pack(side="left", padx=10)
    yellow_circle = canvas_yellow.create_oval(5,5,45,45, fill="grey")
    
    canvas_green = tk.Canvas(light_frame, width=50, height=50, bg="#bdc3c7", highlightthickness=0)
    canvas_green.pack(side="left", padx=10)
    green_circle = canvas_green.create_oval(5,5,45,45, fill="grey")
    
    # ---------------- REAL-TIME UPDATE FUNCTION ----------------
    def update_plot(freq_value):
        freq = int(freq_value)
        power = power_slider.get()
        
        # Update spectrum with frequency and power effect
        y = [random.randint(-50, 0) + freq/100 + power/2 for _ in x]
        line.set_ydata(y)
        ax.relim()
        ax.autoscale_view()
        canvas.draw()
        
        # Reset circles
        canvas_red.itemconfig(red_circle, fill="grey")
        canvas_yellow.itemconfig(yellow_circle, fill="grey")
        canvas_green.itemconfig(green_circle, fill="grey")
        
        # Update traffic lights based on frequency
        if freq < 200:
            canvas_red.itemconfig(red_circle, fill="red")
            winsound.Beep(1000, 100)  # Short beep for real-time
        elif 200 <= freq <= 600:
            canvas_yellow.itemconfig(yellow_circle, fill="yellow")
        else:
            canvas_green.itemconfig(green_circle, fill="green")
    
    # Bind sliders to real-time updates
    freq_slider.config(command=update_plot)
    power_slider.config(command=lambda _: update_plot(freq_slider.get()))

# ================= RUN APP =================
show_dashboard("home")
root.mainloop()