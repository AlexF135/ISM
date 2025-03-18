import tkinter as tk

def on_button_click(value):
    if value == "=":
        try:
            result = eval(entry_var.get())
            entry_var.set(result)
        except Exception as e:
            entry_var.set("Error")
    elif value == "Clear":
        entry_var.set("")
    else:
        entry_var.set(entry_var.get() + str(value))

root = tk.Tk()
root.title("Калькулятор")
root.configure(bg="yellow")
root.resizable(0, 0)

entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 24), bg="lightgreen", justify="right")
entry.grid(row=0, column=0, columnspan=4, ipadx=40, ipady=5)

buttons = [
    ("1", 1, 0), ("2", 1, 1), ("3", 1, 2), ("+", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("-", 2, 3),
    ("7", 3, 0), ("8", 3, 1), ("9", 3, 2), ("*", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("Clear", 4, 2), ("/", 4, 3),
    ("=", 5, 2)
]

for (text, row, col) in buttons:
    btn = tk.Button(root, text=text, font=("Arial", 18), bg="blue", fg="white",
                    width=6, height=2, command=lambda t=text: on_button_click(t))
    btn.grid(row=row, column=col, padx=5, pady=5)

root.mainloop()