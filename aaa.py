from numpy import *
from tkinter import *
from math import *
from gc import *
import tkinter.messagebox


def choice3():
    print('введите r1,a,b,r2')
    r1 = str(input('r1\n'))
    R1 = float(r1)
    a = str(input('a\n'))
    A = float(a)
    b = str(input('b\n'))
    B = float(b)
    r2 = str(input('r2\n'))
    R2 = float(r2)
    f = 'sqrt(%s*%s-x*x)' % (r1, r1)  # x^2+y^2=r^2 - окруж с центром в 0 0|верхняя дуга
    f4 = '-sqrt(%s*%s-x*x)' % (r1, r1)  # нижняя дуга

    f2 = '%s+sqrt(%s*%s-(x-%s)*(x-%s))' % (b, r2, r2, a, a)  # верхняя дуга окружности
    f3 = '%s-sqrt(%s*%s-(x-%s)*(x-%s))' % (b, r2, r2, a, a)  # нижняя дуга окружности
    return f, f4, f2, f3, R1, A, B, R2


def choice2():
    print('введите r,k,b')
    r = str(input('r\n'))
    R = float(r)
    k = str(input('k\n'))
    K = float(k)
    b = str(input('b\n'))
    B = float(b)
    f = '1*sqrt(%s*%s-x*x)' % (r, r)
    f3 = '-1*sqrt(%s*%s-x*x)' % (r, r)

    f2 = '%s*x+%s' % (k, b)
    return f, f3, f2, R, K, B


def choice1():
    print('введите a1,b1,c1,a2,b2,c2')
    a1 = str(input('a1\n'))
    A1 = float(a1)
    b1 = str(input('b1\n'))
    B1 = float(b1)
    c1 = str(input('c1\n'))
    C1 = float(c1)
    a2 = str(input('a2\n'))
    A2 = float(a2)
    b2 = str(input('b2\n'))
    B2 = float(b2)
    c2 = str(input('c2\n'))
    C2 = float(c2)
    f = 'acos((%s-%s*tan(x))/%s)' % (c1, a1, b1)

    f2 = 'asin((%s-%s*cos(x))/%s)' % (c2, a2, b2)
    return f, f2, A1, B1, C1, A2, B2, C2


# ff - резерв имени
eps = float(input('введите точность\n'))
choice = int(input('выбор\n'))
if choice == 3:
    color_f = 'yellow'
    color_f4 = 'yellow'
    color_f2 = 'black'
    color_f3 = 'black'
    f, f4, f2, f3, R1, A, B, R2 = choice3()  # получ ур-я для eval
elif choice == 2:
    color_f = 'yellow'  # верхняя
    color_f2 = 'black'
    color_f3 = 'yellow'  # нижняя
    f, f3, f2, R, K, B = choice2()  # получ ур-я для eval
elif choice == 1:
    color_f = 'yellow'
    color_f2 = 'black'
    f, f2, A1, B1, C1, A2, B2, C2 = choice1()  # получ ур-я для eval


def check(arr, arr2, x, y):  # защита от дублей
    result = False
    for i in range(len(arr)):
        if fabs(((arr[i])) - ((x))) < 10 * eps and fabs(((arr2[i])) - (
        (y))) < 10 * eps:  # если коорд удалены больше эпс, то не дубли|||<1 OLD|||<10*eps
            result = True
            break
            # if choice != 1 and choice != 3 and fabs(fabs(arr[i] - x) - fabs(arr2[i] - y)) < eps*10:#это ОТДЕЛЬНОЕ условие для случая с однократным пересечением линией под наклоном с окружностью
            # result = True
            # break
    return result


# count_numbers = get_count(eps)
count_numbers = 3
root = Tk()

canv = Canvas(root, width=1000, height=1000, bg="pink")

left = 0
right = 0
koleso = 0
canv.create_line(500, 1000, 500, 0, width=2, arrow=LAST)
canv.create_line(0, 500, 1000, 500, width=2, arrow=LAST)

if choice == 3:
    for i in range(10000):  # цикл перебора точек
        raschet(i, f, color_f)
        raschet(i, f2, color_f2)
        raschet(i, f3, color_f3)
        raschet(i, f4, color_f4)
elif choice == 1:
    for i in range(10000):  # цикл перебора точек
        raschet(i, f, color_f)
        raschet(i, f2, color_f2)

elif choice == 2:
    for i in range(10000):  # цикл перебора точек
        raschet(i, f, color_f)
        raschet(i, f2, color_f2)
        raschet(i, f3, color_f3)

if choice == 2:
    ii = -500  # от -500
    arr = []
    arr2 = []
    while ii < 500:  # до 500
        if len(arr) == 2:
            break
        elif K == 0 and B == 0 and len(arr) == 1:  # если линия проходит через 0, совпадая с OX, при B == 0
            break
        elif K == 0 and B != 0 and fabs(B - R) < 0.00001 and len(
                arr) == 1:  # если линия пересекает окружность только в 1 точке и K == 0, то есть параллельно OX
            break
        else:
            j = ii
            try:
                y1 = sqrt(R * R - j * j)
                y3 = -sqrt(R * R - j * j)
                y2 = K * j + B
                if fabs(y1 - y2) <= eps:
                    if check(arr, arr2, j, y1) == False:
                        arr.append(round(j, count_numbers))
                        arr2.append(round(y1, count_numbers))
                        print(y1, ':', y2)
                        # print(y1,y2)
                if fabs(y3 - y2) <= eps:
                    if check(arr, arr2, j, y2) == False:
                        arr.append(round(j, count_numbers))
                        arr2.append(round(y2, count_numbers))
                        print(y2, ':', y2)
                        # print(y1,y2)
            except:
                pass
            ii += eps / 10  # x увел на эпсилон(на погрешность)
            # ii+= jj, где jj < eps - много один корней
elif choice == 3:
    ii = -500
    arr = []
    arr2 = []
    while ii < 500:
        if len(arr) == 2:
            break
        elif fabs((fabs(R1) + fabs(R2)) - (sqrt((0 - A) * (0 - A) + (0 - B) * (0 - B)))) < 0.0001 and len(
                arr) == 1:  # две окруж пересеч в 1 точке
            break
        elif A == 0 and B == 0 and fabs(R1 - R2) < 0.00001:  # совпадают
            break
        else:
            j = ii
            try:
                y1 = sqrt(R1 * R1 - j * j)
                y4 = -sqrt(R1 * R1 - j * j)
                y2 = B + sqrt(R2 * R2 - (j - A) * (j - A))
                y3 = B - sqrt(R2 * R2 - (j - A) * (j - A))
                if fabs((y1 - y2)) <= eps:
                    if check(arr, arr2, j, y1) == False:
                        arr.append(round(j, count_numbers))
                        arr2.append(round(y1, count_numbers))
                        print(y1, y2)
                if fabs((y1 - y3)) <= eps:
                    if check(arr, arr2, j, y1) == False:
                        arr.append(round(j, count_numbers))
                        arr2.append(round(y1, count_numbers))
                        print(y1, y3)
                if fabs((y4 - y2)) <= eps:
                    if check(arr, arr2, j, y4) == False:
                        arr.append(round(j, count_numbers))
                        arr2.append(round(y4, count_numbers))
                        print(y4, y2)
                if fabs((y4 - y3)) <= eps:
                    if check(arr, arr2, j, y4) == False:
                        arr.append(round(j, count_numbers))
                        arr2.append(round(y4, count_numbers))
                        print(y4, y3)
            except:
                pass
            ii += eps / 10
elif choice == 1:
    ii = -500
    arr = []
    arr2 = []
    while ii < 500:
        j = ii
        try:
            y1 = acos((C1 - A1 * tan(j)) / B1)
            y2 = asin((C2 - A2 * cos(j)) / B2)
            if fabs((y1 - y2)) <= eps:
                if check(arr, arr2, j, y1) == False:
                    arr.append(round(j, count_numbers))
                    arr2.append(round(y1, count_numbers))
                    print(y1, y2)
        except:
            pass
        ii += eps / 10

flag_okruzhnosti_sovpadayut = 0
if choice == 3:
    if fabs((fabs(R1) + fabs(R2)) - (
    sqrt((0 - A) * (0 - A) + (0 - B) * (0 - B)))) < 0.0001:  # вторая защита от дублей при пересеч окружностей в 1 точке
        arr1_1 = arr[:]
        arr2_2 = arr2[:]
        arr = []
        arr2 = []
        arr.append(arr1_1[0])
        arr2.append(arr2_2[0])
    if A == 0 and B == 0 and fabs(R1 - R2) < 0.00001:  # совпадение окружностей
        flag_okruzhnosti_sovpadayut = 1
        arr = []
        arr2 = []

elif choice == 2:
    if K == 0 and B == 0:  # если линия проходит через 0, совпадая с OX, при B == 0
        arr.append(-arr[0])
        arr2.append(arr2[0])
    elif K == 0 and B != 0:  # если линия пересекает окружность только в 1 точке и K == 0, то есть параллельно OX
        if fabs(B - R) < 0.00001:
            arr1_1 = arr[:]
            arr2_2 = arr2[:]
            arr = []
            arr2 = []
            arr.append(arr1_1[0])
            arr2.append(arr2_2[0])

print(arr, arr2)
# tochki_peresech(0.25)
#########
if flag_okruzhnosti_sovpadayut == 1:  # защита от совпадения окружностей
    tkinter.messagebox.showinfo("Уведомление", "Окружности совпадают, множество решений вся окружность")
elif len(arr) > 2:
    tkinter.messagebox.showinfo("Уведомление", "Количесво корней бесконечно, так как чередуется")
elif len(arr) == 0:
    tkinter.messagebox.showinfo("Уведомление", "Решение пустое множество. Либо нет решений, либо необходимо изменить точность")

######


# бинды под левую и правую клавишы, и колесо для возврата
canv.bind('<1>', left)
canv.bind('<2>', koleso)
canv.bind('<3>', right)
#
canv.pack()
root.mainloop()

