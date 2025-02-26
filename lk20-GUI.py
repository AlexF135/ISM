

from tkinter import *

root = Tk()

root.geometry("600x600")
root.resizable(width=False, height=False)
root.title("My first desktop application")
root.iconbitmap('chatgpt.ico')

#root.config(bg='purple')
root['bg'] = 'blue'

def click():
    print("Я кнопка!!!")

btn = Button(root,
             text='ЯЯЯЯЯЯЯЯЯ',
             command=click,
             font='Arial 25',
             width='10',
             height='3',
             bg='yellow',
             activebackground='red',
             activeforeground='white',
             fg='green'
             )
btn.pack()


label = Label(root,
             text='Some text I wanted to add',
             font='Arial 25',
             width='20',
             height='3',
             bg='red',
             fg='black',
              padx='125',
              pady='50'
             )
label.pack()

img = PhotoImage(file='youtube.png')
l_label = Label(root, image=img)
l_label.pack()

enter = Entry(root)
enter.pack()

enter.insert(0, 'Enter something')
enter.insert(END, ' here')

root.mainloop()