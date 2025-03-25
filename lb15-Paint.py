import tkinter as tk
from tkinter import colorchooser, filedialog
from PIL import ImageGrab

def start_paint(event):
    global last_x, last_y
    last_x, last_y = event.x, event.y

def draw(event):
    global last_x, last_y
    canvas.create_line(last_x, last_y, event.x, event.y, fill=color, width=brush_size.get(), capstyle=tk.ROUND, smooth=True)
    last_x, last_y = event.x, event.y

def change_color():
    global color
    color = colorchooser.askcolor(color=color)[1]

def clear_canvas():
    canvas.delete("all")

def save_canvas():
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if file_path:
        x = root.winfo_rootx() + canvas.winfo_x()
        y = root.winfo_rooty() + canvas.winfo_y()
        x1 = x + canvas.winfo_width()
        y1 = y + canvas.winfo_height()
        ImageGrab.grab().crop((x, y, x1, y1)).save(file_path, "PNG")

def open_canvas():
    file_path = filedialog.askopenfilename(filetypes=[("PNG files", "*.png")])
    if file_path:
        img = tk.PhotoImage(file=file_path)
        canvas.create_image(0, 0, anchor=tk.NW, image=img)
        canvas.image = img

root = tk.Tk()
root.title("My Paint")

color = "black"

canvas = tk.Canvas(root, bg="white", width=500, height=400)
canvas.pack(fill=tk.BOTH, expand=True)

canvas.bind("<Button-1>", start_paint)
canvas.bind("<B1-Motion>", draw)

frame = tk.Frame(root)
frame.pack()

btn_color = tk.Button(frame, text="Change Color", command=change_color)
btn_color.pack(side=tk.LEFT, padx=5)

btn_clear = tk.Button(frame, text="Clear", command=clear_canvas)
btn_clear.pack(side=tk.LEFT, padx=5)

brush_size = tk.Scale(frame, from_=1, to=10, orient=tk.HORIZONTAL, label="Brush Size")
brush_size.set(5)
brush_size.pack(side=tk.LEFT, padx=5)

menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_canvas)
file_menu.add_command(label="Save", command=save_canvas)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

root.mainloop()
