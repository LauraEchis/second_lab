import math
import pylab
from matplotlib import mlab
import tkinter
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import *
from matplotlib.widgets import TextBox
from matplotlib.widgets import Button
import matplotlib.lines as lines


class Calculator:
    @staticmethod
    def isfloat(value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    @staticmethod
    def first(text):
        arr = []
        arr2 = text.split(",")
        if len(arr2) >= 6:
            for i in range(6):
                arr.append(float(arr2[i]))
        else:
            for i in range(6):
                arr.append(0)
        a1 = arr[0]
        b1 = arr[1]
        c1 = arr[2]
        a2 = arr[3]
        b2 = arr[4]
        c2 = arr[5]
        try:

            ax = plt.subplot(111)
            t = np.arange(-10, 10, 0.001)
            a = -10
            while a < 10:
                try:
                    f = np.arccos((c1 - a1 * np.tan(t)) / b2) + 2 * np.pi * a
                    f2 = np.arcsin((c2 - a2 * np.cos(t)) / b2) + 2 * np.pi * a
                    f3 = -np.arccos((c1 - a1 * np.tan(t)) / b1) + 2 * np.pi * a
                    f4 = np.pi - np.arcsin((c2 - a2 * np.cos(t)) / b2) + 2 * np.pi * a
                except BaseException:
                    f = 0
                    f2 = 0
                    f3 = 0
                    f4 = 0
                x = np.arange(0, 1000)
                y = np.arange(0, 1000)
                idx = np.argwhere(np.diff(np.sign(f - f2)) != 0).reshape(-1) + 0
                idx2 = np.argwhere(np.diff(np.sign(f3 - f4)) != 0).reshape(-1) + 0
                line, = plt.plot(t, f, 'b')
                line, = plt.plot(t, f2, 'r')
                line, = plt.plot(t, f3, 'b')
                line, = plt.plot(t, f4, 'r')
                print (idx)
                print (idx2)
                a += 1

            x_line = [-100, 100]
            y_line = [0, 0]

            x_line_1 = [0, 0]
            y_line_1 = [-100, 100]

            plt.ylim(-10, 10)
            plt.xlim(-10, 10)
            ax.grid(color='grey', linestyle='-', linewidth=0.5)
            line, = plt.plot(x_line, y_line, 'black', linestyle='-', linewidth=1)
            line, = plt.plot(x_line_1, y_line_1, 'black', linestyle='-', linewidth=1)

            plt.show()
        except:
            print("Неожиданная ошибка.")

    @staticmethod
    def second(text):
        try:

            arr = []
            arr2 = text.split(",")
            if len(arr2) >= 3:
                for i in range(3):
                    arr.append(float(arr2[i]))
            else:
                for i in range(3):
                    arr.append(0)
            r = arr[0]
            k = arr[1]
            b = arr[2]
            circle2 = plt.Circle((0, 0), r, color='b', fill=False)
            fig = plt.figure()
            ax = fig.add_subplot(111)
            x = [-100, 100]
            y = [-100 * k + b, 100 * k + b]
            line, = ax.plot(x, y, picker=5)
            ax.add_artist(circle2)
            ax.grid(color='grey', linestyle='-', linewidth=0.5)
            plt.ylim(-30, 30)
            plt.xlim(-30, 30)
            plt.show()
        except:
            return ("Неверно введены данные")

    @staticmethod
    def third(text):
        try:
            arr = []
            arr2 = text.split(",")
            if len(arr2) >= 4:
                for i in range(4):
                    arr.append(float(arr2[i]))
            else:
                for i in range(4):
                    arr.append(0)
            r1 = arr[0]
            x1 = arr[1]
            y2 = arr[2]
            r2 = arr[3]
            circle1 = plt.Circle((0, 0), r1, color='b', fill=False)
            circle2 = plt.Circle((x1, y2), r2, color='r', fill=False)
            fig = plt.figure()
            ax = fig.add_subplot(111)
            ax.add_artist(circle1)
            ax.add_artist(circle2)
            ax.grid(color='grey', linestyle='-', linewidth=0.5)
            plt.ylim(-30, 40)
            plt.xlim(-30, 40)
            plt.show()
        except:
            print("Неожиданная ошибка.")

    @staticmethod
    def first_equation(text):

        arr = []
        arr2 = text.split(",")
        if len(arr2) == 6:
            for i in range(6):
                arr.append(float(arr2[i]))
        else:
            for i in range(6):
                arr.append(0)
        a1 = arr[0]
        b1 = arr[1]
        c1 = arr[2]
        a2 = arr[3]
        b2 = arr[4]
        c2 = arr[5]
        print(arr)
        x = -math.pi
        x1 = 0
        pii_i2 = math.pi
        res_x_1 = []
        res_y_1 = []

        res_x = []
        res_y = []
        while x < math.pi:
            try:
                y_arccos_1 = math.acos((c1 - a1 * math.tan(x)) / b1)
                y_arccos_2 = -math.acos((c1 - a1 * math.tan(x)) / b1)

                y_arcsin_1 = math.asin((c2 - a2 * math.cos(x)) / b2)
                y_arcsin_2 = math.pi - math.asin((c2 - a2 * math.cos(x)) / b2)

                mult1 = math.fabs(y_arccos_1 - y_arcsin_1)
                mult2 = math.fabs(y_arccos_1 - y_arcsin_2)
                mult3 = math.fabs(y_arccos_2 - y_arcsin_1)
                mult4 = math.fabs(y_arccos_2 - y_arcsin_2)

                if mult1 < 0.01 or mult2 < 0.01:
                    if round(x, 1) not in res_x_1 and round(y_arccos_1, 1) not in res_y_1:
                        if round(x, 2) == -0.00:
                            res_x.append(0.00)
                            res_y.append(y_arccos_1)
                            res_x_1.append(0.0)
                            res_y_1.append(round(y_arccos_1, 1))
                        elif round(y_arccos_1, 2) == -0.00:
                            res_x.append(x)
                            res_y.append(0.00)
                            res_x_1.append(round(x, 1))
                            res_y_1.append(0.0)

                        else:
                            res_x.append(x)
                            res_y.append(y_arccos_1)
                            res_x_1.append(round(x, 1))
                            res_y_1.append(round(y_arccos_1, 1))

                if mult3 < 0.01 or mult4 < 0.01:
                    if round(x, 1) not in res_x_1 and round(y_arccos_2, 1) not in res_y_1:
                        if round(x, 2) == -0.00:
                            res_x.append(0.00)
                            res_y.append(y_arccos_2)
                            res_x_1.append(0.0)
                            res_y_1.append(round(y_arccos_2, 1))
                        elif round(y_arccos_1, 2) == -0.00:
                            res_x.append(x)
                            res_y.append(0.00)
                            res_x_1.append(round(x, 1))
                            res_y_1.append(0.0)

                        else:
                            res_x.append(x, 2)
                            res_y.append(y_arccos_2, 2)
                            res_x_1.append(round(x, 1))
                            res_y_1.append(round(y_arccos_2, 1))

                            # print(str(round(x, 2)) + " " + str(round(y_arccos_2, 2)))
            except BaseException:
                pass
            x += 0.0001

        if len(res_x) == 0:
            return ("Общих точек нет")
        elif len(res_x) == 1:
            return ("Одна общая точка" + str(res_x[0]) + " " + str(res_y[0]))
        else:
            return ("Две общие точки на расстоянии 2πk" + '\n' + str(res_x[0]) + " " + str(res_y[0]) + '\n' + str(
                res_x[1]) + " " + str(res_y[1]))

    @staticmethod
    def second_equation(text):
        arr = []
        arr2 = text.split(",")
        if len(arr2) == 3:
            for i in range(3):
                arr.append(float(arr2[i]))
        else:
            for i in range(3):
                arr.append(0)
        r = arr[0]
        b = -1
        a = arr[1]
        c = arr[2]
        # return (r + " " + b + " " + a + " " + c)
        x0 = -a * c / (a * a + b * b)
        y0 = -b * c / (a * a + b * b)
        if (c * c > r * r * (a * a + b * b) + 0.001):
            return ("Общих точек нет")
        elif (math.fabs(c * c - r * r * (a * a + b * b)) < 0.001):

            return ("Одна общая точка" + x0 + " " + y0)
        else:
            d = r * r - c * c / (a * a + b * b)
            mult = math.sqrt(d / (a * a + b * b))
            ax = x0 + b * mult
            bx = x0 - b * mult
            ay = y0 - a * mult
            by = y0 + a * mult
            return ("Две общие точки" + '\n' + str(ax) + " " + str(ay) + '\n' + str(bx) + " " + str(by))

    @staticmethod
    def third_equation(text):
        arr = []
        arr2 = text.split(",")
        if len(arr2) >= 4:
            for i in range(4):
                arr.append(float(arr2[i]))
        else:
            for i in range(4):
                arr.append(0)
        r11 = arr[0]
        x1 = arr[1]
        y1 = arr[2]
        r22 = arr[3]

        if x1 == 0 and y1 == 0 and r11 == r22:
            return ("Бесчисленное множество точек")
        else:
            a = -2 * x1
            b = -2 * y1
            c = pow(x1, 2) + pow(y1, 2) + pow(r11, 2) - pow(r22, 2)

            x0 = -a * c / (a * a + b * b)
            y0 = -b * c / (a * a + b * b)

            if c * c > r11 * r11 * (a * a + b * b) + 0.01:
                return ("Общих точек нет")
            elif abs(c * c - r11 * r11 * (a * a + b * b)) < 0.01:
                return ("Одна общая точка" + x0 + " " + y0)
            else:
                d = r11 * r11 - c * c / (a * a + b * b)
                mult = math.sqrt(d / (a * a + b * b))
                ax = x0 + b * mult
                bx = x0 - b * mult
                ay = y0 - a * mult
                by = y0 + a * mult
                return ("Две общие точки" + '\n' + str(ax) + " " + str(ay) + '\n' + str(bx) + " " + str(by))

                # a = -2 * a1
                # b = -2 * b1
                # c = math.pow(a1, 2) + math.pow(b1, 2) + math.pow(r11, 2) - math.pow(r22, 2)
                # if (c == 0):
                #
                #     if (r11 == r22):
                #         return ("Бесчисленное множество точек")
                #     else:
                #
                #         return ("Общих точек нет");
                #
                # return second_equation(str(a) + "," + str(b) + "," + str(c) + "," + str(r11))


                #

                # n = int(input("Введите номер уравнения"))
                #
                # calcc = Calculator
                # if n == 1:
                #     calcc.first("2,2,2,2,2,2")
                # elif n == 2:
                #     calcc.second("20,2,3")
                #     print(calcc.second_equation("20,2,3"))
                # elif n == 3:
                #     calcc.third("20,10,10,20")
                #     print(calcc.third_equation("20,10,10,20"))
