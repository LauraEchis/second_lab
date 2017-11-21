import matplotlib.pyplot as plt
from matplotlib.patches import *


class Calculator:
    @staticmethod
    def isfloat(value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    @staticmethod
    def first(text, res):
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
                    f = np.arccos((c1 - a1 * np.tan(t)) / b1) + 2 * np.pi * a
                    f2 = np.arcsin((c2 - a2 * np.cos(t)) / b2) + 2 * np.pi * a
                    f3 = -np.arccos((c1 - a1 * np.tan(t)) / b1) + 2 * np.pi * a
                    f4 = np.pi - np.arcsin((c2 - a2 * np.cos(t)) / b2) + 2 * np.pi * a
                except BaseException:
                    print(" ")
                    # f = 0
                    # f2 = 0
                    # f3 = 0
                    # f4 = 0
                # x = np.arange(0, 1000)
                # y = np.arange(0, 1000)
                # idx = np.argwhere(np.diff(np.sign(f - f2)) != 0).reshape(-1) + 0
                # idx2 = np.argwhere(np.diff(np.sign(f3 - f4)) != 0).reshape(-1) + 0
                plt.plot(t, f, 'b')
                plt.plot(t, f2, 'r')
                plt.plot(t, f3, 'b')
                plt.plot(t, f4, 'r')
                # print (idx)
                # print (idx2)
                a += 1

            x_line = [-100, 100]
            y_line = [0, 0]

            x_line_1 = [0, 0]
            y_line_1 = [-100, 100]

            plt.ylim(-10, 10)
            plt.xlim(-10, 10)
            ax.grid(color='grey', linestyle='-', linewidth=0.5)
            plt.plot(x_line, y_line, 'black', linestyle='-', linewidth=1)
            plt.plot(x_line_1, y_line_1, 'black', linestyle='-', linewidth=1)

            if len(res) >= 2:
                # ax.add_artist(plt.Circle((res[0], res[1]), r1/10, color="g", fill=True))
                a1 = res[0]
                b1 = res[1]

                while True:
                    a1 -= 2 * math.pi
                    if a1 >= -15:
                        break
                a_reserved = a1
                while True:
                    b1 -= 2 * math.pi
                    if b1 <= -65:
                        break
                while b1 <= 60:
                    while a1 <= 10:
                        ax.plot(a1, b1, 'x', color='g', )
                        a1 += 2 * math.pi
                    b1 += 2 * math.pi
                    a1 = a_reserved

            if len(res) > 2:
                # ax.add_artist(plt.Circle((res[2], res[3]), r2/10, color="g", fill=True))
                a2 = res[2]
                b2 = res[3]

                while True:
                    a2 -= 2 * math.pi
                    if a2 >= -15:
                        break
                a2_reserved = a2
                print(a2)
                while True:
                    b2 -= 2 * math.pi
                    if b2 <= -65:
                        break
                print(b2)
                while b2 <= 60:
                    while a2 <= 15:
                        ax.plot(a2, b2, 'x', color='g', )
                        a2 += 2 * math.pi
                    b2 += 2 * math.pi
                    a2 = a2_reserved

            plt.show()
        except:
            print("Неожиданная ошибка.")

    @staticmethod
    def second(text, res):
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

            if len(res) >= 2:
                print(len(res))
                # ax.add_artist(plt.Circle((res[0], res[1]), r1/10, color="g", fill=True))
                ax.plot(res[0], res[1], 'x', color='g', )
            if len(res) > 2:
                # ax.add_artist(plt.Circle((res[2], res[3]), r2/10, color="g", fill=True))
                ax.plot(res[2], res[3], 'x', color='g')

            plt.show()
        except:
            print("Неожиданная ошибка.")

    @staticmethod
    def third(text, res):
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
            if len(res) >= 2:
                # ax.add_artist(plt.Circle((res[0], res[1]), r1/10, color="g", fill=True))
                ax.plot(res[0], res[1], 'x', color='g', )
            if len(res) > 2:
                # ax.add_artist(plt.Circle((res[2], res[3]), r2/10, color="g", fill=True))
                ax.plot(res[2], res[3], 'x', color='g')
            plt.show()
        except:
            print("Неожиданная ошибка.")

    @staticmethod
    def first_equation(text):

        arr = []
        arr2 = text.split(",")
        if len(arr2) == 7:
            for i in range(7):
                arr.append(arr2[i])
        else:
            for i in range(6):
                arr.append(0)
            arr.append(0.01)
        a1 = float(arr[0])
        b1 = float(arr[1])
        c1 = float(arr[2])
        a2 = float(arr[3])
        b2 = float(arr[4])
        c2 = float(arr[5])
        if Calculator.isfloat(arr[6]):
            acc = float(arr[6])
        else:
            acc = 0.01
        if str(acc).isdigit():
            acc1 = 10 ** (-acc)
        else:
            acc1 = 0.0001
            acc = 4
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
            x += acc1

        if len(res_x) == 0:
            # return ("Общих точек нет")
            return (0)
        elif len(res_x) == 1:
            res_arr = (res_x[0], res_y[0])
            return res_arr
            # return ("Одна общая точка" + str(res_x[0]) + " " + str(res_y[0]))

        else:
            res_arr = (res_x[0], res_y[0], res_x[1], res_y[1])
            return res_arr
            # return ("Две общие точки на расстоянии 2πk" + '\n' + str(res_x[0]) + " " + str(res_y[0]) + '\n' + str(
            #     res_x[1]) + " " + str(res_y[1]))

    @staticmethod
    def second_equation(text):
        arr = []
        arr2 = text.split(",")
        if len(arr2) == 4:
            for i in range(4):
                arr.append(arr2[i])
        else:
            for i in range(3):
                arr.append(0)
            arr.append(0.01)
        r = float(arr[0])
        b = -1
        a = float(arr[1])
        c = float(arr[2])

        if Calculator.isfloat(arr[3]):
            acc = float(arr[3])
        else:
            acc = 0.01
        if str(acc).isdigit():
            acc1 = 10 ** (-acc)
        else:
            acc1 = 0.001
            acc = 3
        # return (r + " " + b + " " + a + " " + c)
        x0 = -a * c / (a * a + b * b)
        y0 = -b * c / (a * a + b * b)
        if (c * c > r * r * (a * a + b * b) + acc1):
            return 0
            # return ("Общих точек нет")
        elif (math.fabs(c * c - r * r * (a * a + b * b)) < acc1):
            res_arr = (x0, y0)
            return (res_arr)

            # return ("Одна общая точка" + x0 + " " + y0)
        else:
            d = r * r - c * c / (a * a + b * b)
            mult = math.sqrt(d / (a * a + b * b))
            ax = x0 + b * mult
            bx = x0 - b * mult
            ay = y0 - a * mult
            by = y0 + a * mult

            res_arr = (ax, ay, bx, by)
            return (res_arr)

            # return ("Две общие точки" + '\n' + str(ax) + " " + str(ay) + '\n' + str(bx) + " " + str(by))

    @staticmethod
    def third_equation(text):
        arr = []
        arr2 = text.split(",")
        if len(arr2) >= 5:
            for i in range(5):
                arr.append(arr2[i])
        else:
            for i in range(4):
                arr.append(0)
            arr.append(0.01)
        r11 = float(arr[0])
        x1 = float(arr[1])
        y1 = float(arr[2])
        r22 = float(arr[3])
        if Calculator.isfloat(arr[4]):
            acc = float(arr[4])
        else:
            acc = 0.01
        if str(acc).isdigit():
            acc1 = 10 ** (-acc)
        else:
            acc1 = 0.001
            acc = 3

        if x1 == 0 and y1 == 0 and r11 == r22:
            return [-1]
        else:
            a = -2 * x1
            b = -2 * y1
            c = pow(x1, 2) + pow(y1, 2) + pow(r11, 2) - pow(r22, 2)

            x0 = -a * c / (a * a + b * b)
            y0 = -b * c / (a * a + b * b)

            if c * c > r11 * r11 * (a * a + b * b) + acc1:
                return [0]
                # return ("Общих точек нет")
            elif abs(c * c - r11 * r11 * (a * a + b * b)) < acc1:
                res_arr = [x0, y0]
                return (res_arr)
                # return ("Одна общая точка" + x0 + " " + y0)
            else:
                d = r11 * r11 - c * c / (a * a + b * b)
                mult = math.sqrt(d / (a * a + b * b))
                ax = x0 + b * mult
                bx = x0 - b * mult
                ay = y0 - a * mult
                by = y0 + a * mult
                res_arr = [ax, ay, bx, by]
                return (res_arr)
                # return ("Две общие точки" + '\n' + str(ax) + " " + str(ay) + '\n' + str(bx) + " " + str(by))

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
