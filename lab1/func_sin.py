from matplotlib import pyplot as plt
import numpy as np
import math

class sin():
    def __init__(self):
        self.a = 1
        self.b = 4
        self.h = 0.00001
        self.n = (self.b - self.a) / self.h

    def difference_derivative_right_sin(self):
        return [(np.sin(x + self.h) - np.sin(x)) / self.h for x in np.arange(-np.pi, np.pi + self.h, self.h)]

    def difference_derivative_left_sin(self):
        return [(np.sin(x) - np.sin(x - self.h)) / self.h for x in np.arange(-np.pi, np.pi + self.h, self.h)]

    def interpolation_sin(self):
        return [(np.sin(x + 1) - np.sin(x - 1)) / 2 * self.h for x in np.arange(-np.pi, np.pi + self.h, self.h)]

    def sco_sin(self, array):
        sco = 0
        average_value = sum(array) / len(array)
        for x in range(len(array)):
            sco = sco + math.sqrt((1 / (len(array) - 1))) * (array[x] - average_value) ** 2
            return sco

    def sqrt_s_sin(self):
        s = 0
        for x in np.arange(-np.pi, np.pi + self.h, self.h):
            s = s + self.h*np.sin(x-1)
        return s

    def trap_s_sin(self):
        s = 0
        for x in np.arange(-np.pi, np.pi + self.h, self.h):
            s = s + self.h/2 * (np.sin(x-1) + np.sin(x))
        return s

    def simpsons_s_sin(self):
        s = 0
        for x in np.arange(-np.pi, np.pi + self.h, self.h):
            s = s + self.h/4 * (np.sin(x-1) + 4 * np.sin(x-0.5)+np.sin(x))
        return s

    def draw(self):

        phi = np.linspace(-np.pi, np.pi, 628320)

        # производные от функции синуса
        array_difference_derivative_right = self.difference_derivative_right_sin()
        array_difference_derivative_left = self.difference_derivative_left_sin()
        array_interpolation = self.interpolation_sin()

        #графики

        figure, (axis1, axis2, axis3) = plt.subplots(1, 3)
        axis1.plot(phi, array_difference_derivative_right)
        axis1.set_title("difference derivative right", fontsize=7)
        axis1.grid()
        axis1.set_xlabel('X')
        axis1.set_ylabel('Y')


        axis2.plot(phi, array_difference_derivative_left)
        axis2.set_title("difference derivative left", fontsize=7)
        axis2.grid()
        axis2.set_xlabel('X')
        axis2.set_ylabel('Y')

        axis3.plot(phi, array_interpolation)
        axis3.set_title("interpolation", fontsize=7)
        axis3.grid()
        axis3.set_xlabel('X')
        axis3.set_ylabel('Y')


        # среднеквадратичное отклонение
        print(str(self.sco_sin(array_difference_derivative_right)) + " среднеквадратичное отклонение правой производной синуса")
        print(str(self.sco_sin(array_difference_derivative_left))+ " среднеквадратичное отклонение левой производной синуса")
        print(str(self.sco_sin(array_interpolation)) + " среднеквадратичное отклонение центральной производной синуса")

        # нахождение площадей
        print(str(self.sqrt_s_sin())+ " площадь синуса 1")
        print(str(self.trap_s_sin()) + " площадь синуса 2")
        print(str(self.simpsons_s_sin())+ " площадь синуса 3")

        plt.show()

