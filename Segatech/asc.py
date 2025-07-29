import tkinter as tk
from tkinter import ttk
from datetime import datetime
import math
import sys

# === CALCULATION FUNCTIONS ===
def calculate_basic(entry1, entry2, op_box, result_var):
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        op = op_box.get()
        if op == "+": res = a + b
        elif op == "-": res = a - b
        elif op == "*": res = a * b
        elif op == "/": res = a / b if b != 0 else "Divide by zero"
        elif op == "%": res = a % b
        else: res = "Invalid operation"
        result_var.set(f"Result: {res}")
    except:
        result_var.set("Error")

def calculate_sci(entry, op_box, result_var):
    try:
        val = float(entry.get())
        op = op_box.get()
        if op == "sin": res = math.sin(math.radians(val))
        elif op == "cos": res = math.cos(math.radians(val))
        elif op == "tan": res = math.tan(math.radians(val))
        elif op == "log10": res = math.log10(val)
        elif op == "ln": res = math.log(val)
        elif op == "√": res = math.sqrt(val)
        elif op == "exp": res = math.exp(val)
        elif op == "π×": res = math.pi * val
        elif op == "e×": res = math.e * val
        else: res = "Unknown"
        result_var.set(f"Result: {res}")
    except:
        result_var.set("Error")

def calculate_date(e1, e2, result_var):
    try:
        d1 = datetime.strptime(e1.get(), "%Y-%m-%d")
        d2 = datetime.strptime(e2.get(), "%Y-%m-%d")
        delta = abs((d2 - d1).days)
        result_var.set(f"Days between: {delta}")
    except:
        result_var.set("Format: YYYY-MM-DD")

def convert_units(entry, from_box, to_box, result_var):
    try:
        val = float(entry.get())
        from_u = from_box.get()
        to_u = to_box.get()
        if from_u == "C" and to_u == "F": res = val * 9/5 + 32
        elif from_u == "F" and to_u == "C": res = (val - 32) * 5/9
        elif from_u == "km" and to_u == "mi": res = val * 0.621371
        elif from_u == "mi" and to_u == "km": res = val / 0.621371
        elif from_u == "kg" and to_u == "lb": res = val * 2.20462
        elif from_u == "lb" and to_u == "kg": res = val / 2.20462
        else: res = "Invalid"
        result_var.set(f"Converted: {res}")
    except:
        result_var.set("Error")

# === CALCULATOR APP ===
def launch_calculator():
    root = tk.Tk()
    root.title("Segacopter Technology: FutureCalc v1.0")
    root.attributes("-fullscreen", True)
    root.configure(bg="#121212")

    # Add close handler
    root.protocol("WM_DELETE_WINDOW", lambda: root.destroy())

    tabs = ttk.Notebook(root)
    tabs.pack(fill="both", expand=True, padx=20, pady=20)

    # === Basic Math Tab ===
    basic_tab = tk.Frame(tabs, bg="#202020")
    tabs.add(basic_tab, text="🧮 Basic Math")

    tk.Label(basic_tab, text="First Number:", bg="#202020", fg="white", font=("Segoe UI", 12)).pack(pady=5)
    basic_entry1 = tk.Entry(basic_tab, font=("Segoe UI", 12)); basic_entry1.pack()
    tk.Label(basic_tab, text="Second Number:", bg="#202020", fg="white", font=("Segoe UI", 12)).pack(pady=5)
    basic_entry2 = tk.Entry(basic_tab, font=("Segoe UI", 12)); basic_entry2.pack()
    tk.Label(basic_tab, text="Operation:", bg="#202020", fg="white", font=("Segoe UI", 12)).pack(pady=5)
    basic_op = ttk.Combobox(basic_tab, values=["+", "-", "*", "/", "%"]); basic_op.pack()
    basic_result = tk.StringVar()
    tk.Button(basic_tab, text="Calculate", command=lambda: calculate_basic(basic_entry1, basic_entry2, basic_op, basic_result), bg="lime", fg="black").pack(pady=10)
    tk.Label(basic_tab, textvariable=basic_result, bg="#202020", fg="cyan", font=("Segoe UI", 14)).pack()

    # === Scientific Tab ===
    sci_tab = tk.Frame(tabs, bg="#202020")
    tabs.add(sci_tab, text="🧪 Scientific")
    tk.Label(sci_tab, text="Number:", bg="#202020", fg="white", font=("Segoe UI", 12)).pack(pady=5)
    sci_entry = tk.Entry(sci_tab, font=("Segoe UI", 12)); sci_entry.pack()
    tk.Label(sci_tab, text="Function:", bg="#202020", fg="white", font=("Segoe UI", 12)).pack(pady=5)
    sci_op = ttk.Combobox(sci_tab, values=["sin", "cos", "tan", "log10", "ln", "√", "exp", "π×", "e×"]); sci_op.pack()
    sci_result = tk.StringVar()
    tk.Button(sci_tab, text="Calculate", command=lambda: calculate_sci(sci_entry, sci_op, sci_result), bg="cyan", fg="black").pack(pady=10)
    tk.Label(sci_tab, textvariable=sci_result, bg="#202020", fg="lime", font=("Segoe UI", 14)).pack()

    # === Date Tab ===
    date_tab = tk.Frame(tabs, bg="#202020")
    tabs.add(date_tab, text="📅 Date Calculator")
    tk.Label(date_tab, text="Date 1 (YYYY-MM-DD):", bg="#202020", fg="white", font=("Segoe UI", 12)).pack(pady=5)
    date_entry1 = tk.Entry(date_tab, font=("Segoe UI", 12)); date_entry1.pack()
    tk.Label(date_tab, text="Date 2 (YYYY-MM-DD):", bg="#202020", fg="white", font=("Segoe UI", 12)).pack(pady=5)
    date_entry2 = tk.Entry(date_tab, font=("Segoe UI", 12)); date_entry2.pack()
    date_result = tk.StringVar()
    tk.Button(date_tab, text="Calculate", command=lambda: calculate_date(date_entry1, date_entry2, date_result), bg="orange", fg="black").pack(pady=10)
    tk.Label(date_tab, textvariable=date_result, bg="#202020", fg="cyan", font=("Segoe UI", 14)).pack()

    # === Unit Conversion Tab ===
    unit_tab = tk.Frame(tabs, bg="#202020")
    tabs.add(unit_tab, text="🔁 Unit Conversion")
    tk.Label(unit_tab, text="Value:", bg="#202020", fg="white", font=("Segoe UI", 12)).pack(pady=5)
    unit_entry = tk.Entry(unit_tab, font=("Segoe UI", 12)); unit_entry.pack()
    tk.Label(unit_tab, text="From Unit:", bg="#202020", fg="white", font=("Segoe UI", 12)).pack(pady=5)
    unit_from = ttk.Combobox(unit_tab, values=["C", "F", "km", "mi", "kg", "lb"]); unit_from.pack()
    tk.Label(unit_tab, text="To Unit:", bg="#202020", fg="white", font=("Segoe UI", 12)).pack(pady=5)
    unit_to = ttk.Combobox(unit_tab, values=["C", "F", "km", "mi", "kg", "lb"]); unit_to.pack()
    unit_result = tk.StringVar()
    tk.Button(unit_tab, text="Convert", command=lambda: convert_units(unit_entry, unit_from, unit_to, unit_result), bg="#55f", fg="white").pack(pady=10)
    tk.Label(unit_tab, textvariable=unit_result, bg="#202020", fg="lime", font=("Segoe UI", 14)).pack()

    exit_btn = tk.Button(root, text="❌ Exit", command=root.destroy, bg="#333", fg="white", font=("Segoe UI", 10, "bold"))
    exit_btn.place(relx=0.97, rely=0.01, anchor="ne")  # Top-right corner


    root.mainloop()

# === LICENSE AGREEMENT WINDOW ===
def show_eula():
    eula_win = tk.Tk()
    eula_win.title("License Agreement")
    eula_win.attributes("-fullscreen", True)
    eula_win.configure(bg="#1c1c1c")

    # Close button handler
    def disagree():
        eula_win.destroy()
        sys.exit()

    def agree():
        eula_win.destroy()
        launch_calculator()

    eula_win.protocol("WM_DELETE_WINDOW", disagree)

    tk.Label(eula_win, text="OPEN SOURCE LICENSE AGREEMENT", font=("Segoe UI", 20, "bold"),
             fg="cyan", bg="#1c1c1c").pack(pady=20)

    license_text = (
        "SEGACOPTER TECHNOLOGY - OPEN SOURCE LICENSE\n\n"
        "This software is open source and free to use.\n"
        "You are allowed to:\n"
        "✔️ Use this software for any purpose\n"
        "✔️ Modify the source code\n"
        "✔️ Share it, remix it, or integrate it into your own projects\n\n"
        "You do NOT need to pay, credit, or ask permission.\n"
        "This software is provided 'as-is' with no warranties.\n\n"
        "By clicking 'I Agree', you accept that this is freeware and comes with no liability.\n\n"
        "© 2025 Segacopter Technology — Built for the people!"
    )

    text_box = tk.Text(eula_win, wrap="word", font=("Segoe UI", 12), bg="#2a2a2a", fg="white")
    text_box.insert("1.0", license_text)
    text_box.config(state="disabled")
    text_box.pack(padx=20, pady=10, fill="both", expand=True)

    btn_frame = tk.Frame(eula_win, bg="#1c1c1c")
    btn_frame.pack(pady=20)
    tk.Button(btn_frame, text="I Agree", command=agree, bg="lime", fg="black", font=("Segoe UI", 12)).pack(side="left", padx=20)
    tk.Button(btn_frame, text="I Disagree", command=disagree, bg="red", fg="white", font=("Segoe UI", 12)).pack(side="right", padx=20)

    exit_btn = tk.Button(eula_win, text="❌ Exit", command=disagree, bg="#333", fg="white", font=("Segoe UI", 10, "bold"))
    exit_btn.place(relx=0.97, rely=0.01, anchor="ne")  # Top-right corner


    eula_win.mainloop()

# === START ===
show_eula()
