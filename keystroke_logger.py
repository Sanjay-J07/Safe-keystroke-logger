import tkinter as tk
from datetime import datetime

log_file = "keystrokes.txt"
logging_enabled = False

def start_logging():
    global logging_enabled
    logging_enabled = True
    status_label.config(text="Status: Logging (only inside this window)")

def stop_logging():
    global logging_enabled
    logging_enabled = False
    status_label.config(text="Status: Stopped")

def on_key_press(event):
    if logging_enabled:
        with open(log_file, "a") as f:
            f.write(f"{datetime.now()} - {event.keysym}\n")

# Create window
root = tk.Tk()
root.title("Keystroke Logger (Safe Mode)")
root.geometry("400x200")

title = tk.Label(root, text="Safe Keystroke Logger", font=("Arial", 14))
title.pack(pady=10)

status_label = tk.Label(root, text="Status: Stopped")
status_label.pack(pady=5)

start_btn = tk.Button(root, text="Start Logging", command=start_logging)
start_btn.pack(pady=5)

stop_btn = tk.Button(root, text="Stop Logging", command=stop_logging)
stop_btn.pack(pady=5)

info = tk.Label(root, text="Logs only keys typed in this window.\nFor learning purposes only.")
info.pack(pady=10)

# Bind key press event (ONLY inside this app)
root.bind("<KeyPress>", on_key_press)

root.mainloop()