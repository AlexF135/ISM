import tkinter as tk
from tkinter import messagebox
import time
import threading
import pygame

def check_alarm():
    while True:
        current_time = time.strftime("%H:%M")
        if current_time == alarm_time.get():
            pygame.mixer.init()
            pygame.mixer.music.load("C:/Users/filya/Desktop/Imagine Dragons- Believer.mp3")
            pygame.mixer.music.play()
            messagebox.showinfo("Будильник", "Час прокидатися!")
            break
        time.sleep(30)

def set_alarm():
    threading.Thread(target=check_alarm, daemon=True).start()


root = tk.Tk()
root.title("Будильник")
root.geometry("300x200")

tk.Label(root, text="Встановіть час (ГГ:ХХ):").pack(pady=10)

alarm_time = tk.StringVar()
time_entry = tk.Entry(root, textvariable=alarm_time, font=("Arial", 14))
time_entry.pack(pady=5)

set_button = tk.Button(root, text="Встановити будильник", command=set_alarm)
set_button.pack(pady=10)

root.mainloop()
