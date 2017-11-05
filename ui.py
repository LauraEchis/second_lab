from tkinter import *
from sfsdf import Calculator

calc = Calculator()
root = Tk()
root.title("Решения уравнений")
root.geometry("600x400")
frame1 = Frame(root, bg='green', bd=5)
frame2 = Frame(root, bd=5)
frame3 = Frame(root, bg='green', bd=5)
button1 = Button(frame1, text='test')
# Кароче, я задолбался искать, как отправить туда аргумент. В файле tests правильный код бинда, но без доп аргумента...
# button1.bind('<1>', calc.first(event, ""))

frame1.pack(fill='x', side='left')
frame2.pack(fill='x', )
frame3.pack(fill='x', side='right')

root.mainloop()
