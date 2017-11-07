from tkinter import *
from sfsdf import Calculator

calc = Calculator()
root = Tk()
root.title("Решения уравнений")
root.geometry("600x400")
frame1 = Frame(root, bg='green', bd=5)
frame2 = Frame(root, bg='red', bd=5)
frame3 = Frame(root, bg='green', bd=5)


def first(event):
    calc.first(text=(a1.get() + ',' + b1.get() + ',' + c1.get() + ',' + a2.get() + ',' + b2.get() + ',' + c2.get()))


def second(event):
    calc.second(r.get() + ',' + k.get() + ',' + b.get())


def third(event):
    calc.third(r1.get() + ',' + x.get() + ',' + y.get() + ',' + r2.get())


# Кароче, я задолбался искать, как отправить туда аргумент. В файле tests правильный код бинда, но без доп аргумента...
# button1.bind('<1>', calc.first(event, ""))

a1 = Entry(frame1)
a1.pack()
b1 = Entry(frame1)
b1.pack()
c1 = Entry(frame1)
c1.pack()
a2 = Entry(frame1)
a2.pack()
b2 = Entry(frame1)
b2.pack()
c2 = Entry(frame1)
c2.pack()
button1 = Button(frame1, text='first', width=5, height=2)
button1.bind("<1>", first)
button1.pack()

r = Entry(frame2)
r.pack()
k = Entry(frame2)
k.pack()
b = Entry(frame2)
b.pack()
button2 = Button(frame2, text='second', width=5, height=2)
button2.bind("<1>", second)
button2.pack()

r1 = Entry(frame3)
r1.pack()
x = Entry(frame3)
x.pack()
y = Entry(frame3)
y.pack()
r2 = Entry(frame3)
r2.pack()
button3 = Button(frame3, text='third', width=5, height=2)
button3.bind("<1>", third)
button3.pack()

textbox4 = Text(root, width=100, height=20)
textbox4.grid(row=1, columnspan=3)

frame1.grid(row=0, column=0)
frame2.grid(row=0, column=1)
frame3.grid(row=0, column=2)

root.mainloop()
