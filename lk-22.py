

import tkinter as tk
from tkinter import filedialog, messagebox

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "r", encoding='utf-8') as file:
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(text_area.get(1.0, tk.END))

def exit_editor():
    if messagebox.askokcancel("Вихід", "Ви впевнені, що хочете вийти?"):
        root.destroy()

root = tk.Tk()
root.title("Простий текстовий редактор")
root.geometry("600x400")

text_area = tk.Text(root, font=('Arial', 12))
text_area.pack(expand=1, fill=tk.BOTH)

menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar)
file_menu.add_command(label='Відкрити файл', command=open_file)
file_menu.add_command(label='Зберігтии файл', command=save_file)
file_menu.add_command(label='Вихід', command=exit_editor)

menu_bar.add_cascade(label='Файл', menu=file_menu)
root.config(menu=menu_bar)


root.mainloop()