from tkinter import *

root = Tk()
frame1 = Frame(root, bg='green', bd=5)
frame2 = Frame(root, bg='red', bd=5)


def printer(event):
    button1['bg'] = 'red'
    button2['bg'] = 'green'


def call(event):
    print(event.widget["text"])


button1 = Button(frame1, text=u'Первая кнопка')
button2 = Button(frame2, text=u'Вторая кнопка')
button1.bind('<1>', call)
button2.bind('<1>', call)

frame1.pack(fill='both')
frame2.pack(fill='both')
button1.pack()
button2.pack()
root.mainloop()
