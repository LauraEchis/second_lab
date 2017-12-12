from tkinter import *
from calculator import Calculator

root = Tk()
root.title("Решения уравнений")
root.geometry("875x450")

frame1 = Frame(root, bd=5)
frame2 = Frame(root, bd=5)
frame3 = Frame(root, bd=5)


def first(event):
    text = a1.get() + ',' + b1.get() + ',' + c1.get() + ',' + a2.get() + ',' + b2.get() + ',' + c2.get() + ',' + acc.get()

    if Calculator.isNeededNumber(a1.get()) and Calculator.isNeededNumber(b1.get()) and Calculator.isNeededNumber(
            c1.get()) and Calculator.isNeededNumber(a2.get()) and Calculator.isNeededNumber(
        b2.get()) and Calculator.isNeededNumber(
        c2.get() and Calculator.isNeededNumber(acc.get())):
        res_f = Calculator.first_equation(text)
        acc_print = acc.get()
        res_to_print = []
        if not (Calculator.isNeededNumber(acc_print) and int(acc_print) > 0):
            acc_print = 3
        else:
            acc_print = int(acc_print)
        print(acc_print)
        if len(res_f) == 1:
            vivod.insert(END, '\nПервая система уравнений\n' + "Нет общих точек" + '\n')
            Calculator.first(text, res_f)
        elif len(res_f) == 2:
            vivod.insert(END, '\nПервая система уравнений\n' + str(round(res_f[0], acc_print)) + " " + str(
                round(res_f[1], acc_print)) + "±2πk" + '\n')
            Calculator.first(text, res_f)
        else:
            vivod.insert(END, '\nПервая система уравнений\n' + str(round(float(res_f[0]), acc_print)) + " " + str(
                round(float(res_f[1]), acc_print)) + ", " + str(round(float(res_f[2]), acc_print)) + " "
                         + str(round(float(res_f[3]), acc_print)) + " ±2πk" + '\n')
            Calculator.first(text, res_f)
    else:
        vivod.insert(END, '\nНеверные данные\n')


def second(event):
    text = r.get() + ',' + k.get() + ',' + b.get() + ',' + acc.get()
    if Calculator.isNeededNumber(r.get()) and Calculator.isNeededNumber(k.get()) and Calculator.isNeededNumber(
            b.get() and Calculator.isNeededNumber(acc.get())):
        res_s = Calculator.second_equation(text)
        acc_print = acc.get()
        if not (Calculator.isNeededNumber(acc_print) and int(acc_print) > 0):
            acc_print = 3
        else:
            acc_print = int(acc_print)
        print(acc_print)
        if res_s == 0:
            vivod.insert(END, '\nВторая система уравнений\n' + "Нет общих точек" + '\n')
            Calculator.second(text, -1000)
        elif len(res_s) == 2:
            vivod.insert(END, '\nВторая система уравнений\n' + str(round(res_s[0], acc_print)) + " " + str(
                round(res_s[1], acc_print)) + '\n')
            Calculator.second(text, res_s)
        else:
            vivod.insert(END, '\nВторая система уравнений\n' + str(round(float(res_s[0]), acc_print)) + " " + str(
                round(float(res_s[1]), acc_print)) + ", " + str(round(float(res_s[2]), acc_print)) + " "
                         + str(round(float(res_s[3]), acc_print)) + '\n')
            Calculator.second(text, res_s)
    else:
        vivod.insert(END, '\nНеверные данные\n')


def third(event):
    text = r1.get() + ',' + x.get() + ',' + y.get() + ',' + r2.get() + ',' + acc.get()
    if Calculator.isNeededNumber(r1.get()) and Calculator.isNeededNumber(x.get()) and Calculator.isNeededNumber(
            y.get()) and Calculator.isNeededNumber(
        r2.get() and Calculator.isNeededNumber(acc.get())):
        res_t = Calculator.third_equation(text)

        acc_print = acc.get()
        res_to_print = []
        if not (Calculator.isNeededNumber(acc_print) and int(acc_print) > 0):
            acc_print = 3
        else:
            acc_print = int(acc_print)
        print(acc_print)
        if len(res_t) == 1:
            vivod.insert(END,
                         '\nТретья система уравнений\n' + (
                         "Нет общих точек" if str(res_t[0]) == '0' else "Бесчисленное множество точек") + '\n')
            Calculator.third(text, res_t)
        elif len(res_t) == 2:
            vivod.insert(END, '\nТретья система уравнений. Найдена одна (1) точка\n' + str(
                round(res_t[0], acc_print)) + " " + str(
                round(res_t[1], acc_print)) + '\n')
            Calculator.third(text, res_t)
        else:
            vivod.insert(END, '\nТретья система уравнений. Найдено две (2) точки\n' + str(
                round(float(res_t[0]), acc_print)) + " " + str(
                round(float(res_t[1]), acc_print)) + ", " + str(round(float(res_t[2]), acc_print)) + " "
                         + str(round(float(res_t[3]), acc_print)) + '\n')
            Calculator.third(text, res_t)
    else:
        vivod.insert(END, '\nНеверные данные\n')


a1l = Label(frame1)
a1l['text'] = u'Параметр a1'
a1l.grid(row=0, column=0)
a1 = Entry(frame1)
a1.grid(row=0, column=1)
b1l = Label(frame1)
b1l['text'] = u'Параметр b1'
b1l.grid(row=1, column=0)
b1 = Entry(frame1)
b1.grid(row=1, column=1)
c1l = Label(frame1)
c1l['text'] = u'Параметр c1'
c1l.grid(row=2, column=0)
c1 = Entry(frame1)
c1.grid(row=2, column=1)
a2l = Label(frame1)
a2l['text'] = u'Параметр a2'
a2l.grid(row=3, column=0)
a2 = Entry(frame1)
a2.grid(row=3, column=1)
b2l = Label(frame1)
b2l['text'] = u'Параметр b2'
b2l.grid(row=4, column=0)
b2 = Entry(frame1)
b2.grid(row=4, column=1)
c2l = Label(frame1)
c2l['text'] = u'Параметр c2'
c2l.grid(row=5, column=0)
c2 = Entry(frame1)
c2.grid(row=5, column=1)
button1 = Button(frame1, text='Решить первую систему уравнений')
button1.bind("<1>", first)
button1.grid(row=6, columnspan=2)

r = Entry(frame2)
r.grid(row=0, column=1)
rl = Label(frame2)
rl['text'] = u'Параметр r'
rl.grid(row=0, column=0)
kl = Label(frame2)
kl['text'] = u'Параметр k'
kl.grid(row=1, column=0)
k = Entry(frame2)
k.grid(row=1, column=1)
bl = Label(frame2)
bl['text'] = u'Параметр b'
bl.grid(row=2, column=0)
b = Entry(frame2)
b.grid(row=2, column=1)
button2 = Button(frame2, text='Решить вторую систему уравнений')
button2.bind("<1>", second)
button2.grid(row=3, columnspan=2)

r1l = Label(frame3)
r1l['text'] = u'Параметр r1'
r1l.grid(row=0, column=0)
r1 = Entry(frame3)
r1.grid(row=0, column=1)
xl = Label(frame3)
xl['text'] = u'Параметр x '
xl.grid(row=1, column=0)
x = Entry(frame3)
x.grid(row=1, column=1)
yl = Label(frame3)
yl['text'] = u'Параметр y '
yl.grid(row=2, column=0)
y = Entry(frame3)
y.grid(row=2, column=1)
r2l = Label(frame3)
r2l['text'] = u'Параметр r1'
r2l.grid(row=3, column=0)
r2 = Entry(frame3)
r2.grid(row=3, column=1)
button3 = Button(frame3, text='Решить третью систему уравнений')
button3.bind("<1>", third)
button3.grid(row=4, columnspan=2)

frameforviv = Frame(root)
accl = Label(frameforviv)
accl['text'] = u'Точность (количество знаков после запятой)'
accl.grid(row=0, column=0)
acc = Entry(frameforviv)
acc.grid(row=0, column=1)


def clearViv(event):
    vivod.delete(2.0, END)


cb = Button(frameforviv, text='Зачистить вывод')
cb.bind("<1>", clearViv)
cb.grid(row=1, columnspan=2)

vivod = Text(frameforviv)
vivod.grid(row=2, column=0, columnspan=2)
vivod.insert(1.0, 'Решение систем уравнений\n')
frameforviv["bg"] = "cyan"
frame1["bg"] = "cyan"
frame2["bg"] = "cyan"
frame3["bg"] = "cyan"
frameforviv.grid(row=0, column=1, rowspan=3)
frame1.grid(row=0, column=0)
frame2.grid(row=1, column=0)
frame3.grid(row=2, column=0)

root["bg"] = "cyan"
root.mainloop()
