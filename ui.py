from tkinter import *
from sfsdf import Calculator

calc = Calculator()
root = Tk()
root.title("Решения уравнений")
root.geometry("600x400")
frame1 = Frame(root, bg='green', bd=5)


def first(event):
    textbox4.delete(1.0, END)
    Calculator.first(textbox1.get(1.0,END))


def second(event):
    textbox4.delete(1.0, END)
    textbox4.insert(1.0,Calculator.second_equation(textbox2.get(1.0, END)))
    Calculator.second(textbox2.get(1.0,END))


def third(event):
    textbox4.delete(1.0,END)
    textbox4.insert(1.0, Calculator.third_equation(textbox3.get(1.0, END)))
    Calculator.third(textbox3.get(1.0,END))
# Кароче, я задолбался искать, как отправить туда аргумент. В файле tests правильный код бинда, но без доп аргумента...
# button1.bind('<1>', calc.first(event, ""))

textbox1 = Text(frame1, width = 15, height = 1,bd = 5)
textbox1.pack()
button1 = Button(frame1, text='first', width = 5, height = 2)
button1.bind("<1>",first)
button1.pack()


textbox2 = Text(frame1, width = 15, height = 1)
textbox2.pack()
button2 = Button(frame1, text='second', width = 5, height = 2)
button2.bind("<1>",second)
button2.pack()

textbox3 = Text(frame1, width = 15, height = 1)
textbox3.pack()
button3 = Button(frame1, text='third', width = 5, height = 2)
button3.bind("<1>",third)
button3.pack()

textbox4 = Text(frame1,width = 100,height = 20)
textbox4.pack()

frame1.pack(fill='x', side='left')

root.mainloop()

