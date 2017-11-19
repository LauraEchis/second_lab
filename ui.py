from tkinter import *
from sfsdf import Calculator

root = Tk()
root.title("Решения уравнений")
root.geometry("650x400")
root.resizable(False, False)
frame1 = Frame(root, bd=5)
frame2 = Frame(root, bd=5)
frame3 = Frame(root, bd=5)


def first(event):
    text = a1.get() + ',' + b1.get() + ',' + c1.get() + ',' + a2.get() + ',' + b2.get() + ',' + c2.get()
    if Calculator.isfloat(a1.get()) and Calculator.isfloat(b1.get()) and Calculator.isfloat(
            c1.get()) and Calculator.isfloat(a2.get()) and Calculator.isfloat(b2.get()) and Calculator.isfloat(
        c2.get()):
        res_f = Calculator.first_equation(text)
        vivod.insert(END, '\nПервая система уравнений\n' + str(res_f) + '\n')
        Calculator.first(text, res_f)
    else:
        vivod.insert(END, '\nНеверные данные\n')


def second(event):
    text = r.get() + ',' + k.get() + ',' + b.get()
    if Calculator.isfloat(r.get()) and Calculator.isfloat(k.get()) and Calculator.isfloat(b.get()):
        res_s = Calculator.second_equation(text)
        vivod.insert(END, '\nВторая система уравнений\n' + str(res_s) + '\n')
        Calculator.second(text, res_s)
    else:
        vivod.insert(END, '\nНеверные данные\n')


def third(event):
    text = r1.get() + ',' + x.get() + ',' + y.get() + ',' + r2.get()
    if Calculator.isfloat(r1.get()) and Calculator.isfloat(x.get()) and Calculator.isfloat(
            y.get()) and Calculator.isfloat(r2.get()):
        res_t = Calculator.third_equation(text)
        vivod.insert(END, '\nТретья система уравнений\n' + str(res_t) + '\n')
        Calculator.third(text)
    else:
        vivod.insert(END, '\nНеверные данные\n')


a1l = Label(frame1)
a1l['text'] = u'Введите a1'
a1l.grid(row=0, column=0)
a1 = Entry(frame1)
a1.grid(row=0, column=1)
b1l = Label(frame1)
b1l['text'] = u'Введите b1'
b1l.grid(row=1, column=0)
b1 = Entry(frame1)
b1.grid(row=1, column=1)
c1l = Label(frame1)
c1l['text'] = u'Введите c1'
c1l.grid(row=2, column=0)
c1 = Entry(frame1)
c1.grid(row=2, column=1)
a2l = Label(frame1)
a2l['text'] = u'Введите a2'
a2l.grid(row=3, column=0)
a2 = Entry(frame1)
a2.grid(row=3, column=1)
b2l = Label(frame1)
b2l['text'] = u'Введите b2'
b2l.grid(row=4, column=0)
b2 = Entry(frame1)
b2.grid(row=4, column=1)
c2l = Label(frame1)
c2l['text'] = u'Введите c2'
c2l.grid(row=5, column=0)
c2 = Entry(frame1)
c2.grid(row=5, column=1)
button1 = Button(frame1, text='Решить первую систему уравнений')
button1.bind("<1>", first)
button1.grid(row=6, columnspan=2)

Label(frame2).grid(row=0)
Label(frame2).grid(row=1)
r = Entry(frame2)
r.grid(row=2, column=1)
rl = Label(frame2)
rl['text'] = u'Введите r'
rl.grid(row=2, column=0)
kl = Label(frame2)
kl['text'] = u'Введите k'
kl.grid(row=3, column=0)
k = Entry(frame2)
k.grid(row=3, column=1)
bl = Label(frame2)
bl['text'] = u'Введите b'
bl.grid(row=4, column=0)
b = Entry(frame2)
b.grid(row=4, column=1)
button2 = Button(frame2, text='Решить вторую систему уравнений')
button2.bind("<1>", second)
button2.grid(row=5, columnspan=2)
Label(frame2).grid(row=6)

Label(frame3).grid(row=0)
r1l = Label(frame3)
r1l['text'] = u'Введите r1'
r1l.grid(row=1, column=0)
r1 = Entry(frame3)
r1.grid(row=1, column=1)
xl = Label(frame3)
xl['text'] = u'Введите x '
xl.grid(row=2, column=0)
x = Entry(frame3)
x.grid(row=2, column=1)
yl = Label(frame3)
yl['text'] = u'Введите y '
yl.grid(row=3, column=0)
y = Entry(frame3)
y.grid(row=3, column=1)
r2l = Label(frame3)
r2l['text'] = u'Введите r1'
r2l.grid(row=4, column=0)
r2 = Entry(frame3)
r2.grid(row=4, column=1)
button3 = Button(frame3, text='Решить третью систему уравнений')
button3.bind("<1>", third)
button3.grid(row=5, columnspan=2)
Label(frame3).grid(row=6)

vivod = Text(root)
vivod.grid(row=1, columnspan=3)
vivod.insert(1.0, 'Решение систем:\n')
frame1.grid(row=0, column=0)
frame2.grid(row=0, column=1)
frame3.grid(row=0, column=2)

root.mainloop()
