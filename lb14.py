import tkinter as tk
from tkinter import messagebox
import math


def on_click(choice):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get()) if entry2.get() else None
        result = None

        if choice == "+":
            result = num1 + num2
        elif choice == "-":
            result = num1 - num2
        elif choice == "*":
            result = num1 * num2
        elif choice == "/":
            if num2 == 0:
                messagebox.showerror("Помилка", "Ділення на нуль!")
                return
            result = num1 / num2
        elif choice == "^":
            result = num1 ** num2
        elif choice == "√":
            if num1 < 0:
                messagebox.showerror("Помилка", "Не можна обчислити корінь з від’ємного числа!!")
                return
            result = math.sqrt(num1)

        result_label.config(text=f"Результат: {result}")
    except ValueError:
        messagebox.showerror("Помилка", "Введіть коректні числа!")


root = tk.Tk()
root.title("Калькулятор")
root.geometry("500x700")
root.resizable(width=False, height=False)

tk.Label(root, text="Введіть перше число:", font='Arial 15').pack()
entry1 = tk.Entry(root, width=10, font=("Arial", 20))
entry1.pack()

tk.Label(root, text="Введіть друге число (якщо потрібно):", font='Arial 15').pack()
entry2 = tk.Entry(root, width=10, font=("Arial", 20))
entry2.pack()

buttons = [
    ("+", "+"), ("-", "-"), ("*", "*"), ("/", "/"),
    ("^", "^"), ("√", "√")
]

for text, choice in buttons:
    tk.Button(root, text=text,
              command=lambda op=choice: on_click(op),
              font=("Arial", 14),
              width=5,
              height=2,
              bg="lightblue").pack(pady=5)

result_label = tk.Label(root, text="Результат:", font=("Arial", 25))
result_label.pack(pady=10)

tk.Button(root, text="Вийти",
          command=root.quit,
          font=("Arial", 14),
          bg="red", fg="white",
          width=10,
          height=2).pack(pady=10)

root.mainloop()
