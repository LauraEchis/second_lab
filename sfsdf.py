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
            line, = plt.plot(t, f)
            line, = plt.plot(t, f2)
            line, = plt.plot(t, f3)
            line, = plt.plot(t, f4)
            a += 1
        plt.ylim(-10, 10)
        plt.xlim(-10, 10)
        plt.show()
    except:
        print("Неожиданная ошибка.")


# first("2,2,2,2,2,2")

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
        plt.ylim(-100, 100)
        plt.xlim(-100, 100)
        plt.show()
    except:
        print("Неожиданная ошибка.")


second("20,2,3")
