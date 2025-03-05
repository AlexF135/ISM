

from tkinter import *
from tkinter import messagebox
import random


def No():
    messagebox.showinfo("Опитування", "Ну ні так ні, діло ваше")
    quit()


def motionMouse(event):
    btnYes.place(x=random.randint(0, 700), y=random.randint(0,500))

root = Tk()

root.geometry("800x600")
root.title("Опитування")
root.config(bg='black')
root.resizable(width=False, height=False)


label=Label(root, text='Чи хочете ви отримати 1 000 000 гривень?', font='Arial 20 bold' ).pack()

btnYes=Button(root, text='Так', font='Arial 20 bold')
btnYes.place(x=150, y=200)

btnYes.bind('<Enter>', motionMouse)

btnNo=Button(root, text='Ні', font='Arial 20 bold', command=No)
btnNo.place(x=500, y=200)







root.mainloop()



'''label2 = Label(root, text='123', font='Arial 15', width='10', height='3', bg='yellow', fg='black').pack(side=BOTTOM)
label3 = Label(root, text='123', font='Arial 15', width='10', height='3', bg='green', fg='black').pack(side=LEFT)
label4 = Label(root, text='123', font='Arial 15', width='10', height='3', bg='blue', fg='black').pack(side=RIGHT)'''

#label1 = Label(root, text='123', font='Arial 15', width='10', height='3', bg='red', fg='black').pack(expand=1, fill=BOTH)
#label1 = Label(root, text='123', font='Arial 15', width='10', height='3', bg='red', fg='black').pack(expand=1, anchor=NW)

#label1 = Label(root, text='123', font='Arial 15', width='10', height='3', bg='red', fg='black')
#label1.place(relx=0.5, rely=0.5, anchor=CENTER)

#label1.place(relx=0.5, rely=0.5, anchor=CENTER, relwidth=0.5, relheight=0.5)


'''btn1 = Button(root, text='111', font='Arial 15', bg='red', fg='black', padx=20, pady=20)
btn1.grid(row=0, column=1)

btn2 = Button(root, text='222', font='Arial 15', bg='red', fg='black', padx=64, pady=20)
btn2.grid(row=1, column=1, columnspan=2)

btn3 = Button(root, text='333', font='Arial 15', bg='red', fg='black', padx=20, pady=20)
btn3.grid(row=2, column=0)

btn4 = Button(root, text='444', font='Arial 15', bg='red', fg='black', padx=20, pady=64)
btn4.grid(row=2, column=1, rowspan=2)'''