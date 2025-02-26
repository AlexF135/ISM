


from tkinter import *

root = Tk()

root.geometry("600x600")
root.resizable(width=False, height=False)
root.title("My first desktop application")
root.iconbitmap('chatgpt.ico')
root['bg'] = 'blue'


def add():
    enter.insert(END, 'Hello world!')

def vidalennya():
    enter.delete(0, END)

def get():
    label1['text'] = enter.get()


label1 = Label(root, bg='black', fg='white')
label1.pack()

enter = Entry(root, font='Arial 25', show='*')
enter.insert(0, 'Enter something')
enter.insert(END, ' here')
enter.pack()


btn1 = Button(root, font='Arial 15', text='Insert', command=add)
btn1.pack()

btn2 = Button(root, font='Arial 15', text='Delete', command=vidalennya)
btn2.pack()

btn3 = Button(root, font='Arial 15', text='Get', command=get)
btn3.pack()


root.mainloop()
