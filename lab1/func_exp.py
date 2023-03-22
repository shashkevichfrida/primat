from matplotlib import pyplot as plt
import numpy as np
import math

class exp():
    def __init__(self):
        self.a = 0.00001
        self.b = 4
        self.h = 1
        self.n = (self.b - self.a) / self.h

    def difference_derivative_right_exp(self):
        return [(np.exp(x + self.h) - np.exp(x)) / self.h for x in np.arange(-100, 0)]

    def difference_derivative_left_exp(self):
        return [(np.exp(x) - np.exp(x - self.h)) / self.h for x in np.arange(-100, 0)]

    def interpolation_exp(self):
        return [(np.exp(x + 1) - np.exp(x - 1)) / 2 * self.h for x in np.arange(-100, 0)]

    def sco_exp(self, array):
        sco = 0
        average_value = sum(array) / len(array)
        for x in np.arange(len(array)):
            sco = sco + math.sqrt((1 / (len(array) - 1))) * (array[x] - average_value) ** 2
        return sco

    def sqrt_s_exp(self):
        s = 0
        for x in np.arange(-100, self.h, self.h):
            s = s + self.h * np.exp(x - 1)
        return s

    def trap_s_exp(self):
        s = 0
        for x in np.arange(-100, self.h, self.h):
            s = s + self.h / 2 * (np.exp(x - 1) + np.exp(x))
        return s

    def simpsons_s_exp(self):
        s = 0
        for x in np.arange(-100, self.h, self.h):
            s = s + self.h / 4 * (np.exp(x - 1) + 4 * np.exp(x - 0.5) + np.exp(x))
        return s

    def draw(self):
        array_difference_derivative_right = self.difference_derivative_right_exp()
        array_difference_derivative_left = self.difference_derivative_left_exp()
        array_interpolation = self.interpolation_exp()

        array_x = np.linspace(-100, 0, len(array_difference_derivative_right))

        # среднеквадратичное отклонение
        print(str(self.sco_exp(array_difference_derivative_right)) + " среднеквадратичное отклонение правой производной экспоненты")
        print(str(self.sco_exp(array_difference_derivative_left)) + " среднеквадратичное отклонение левой производной экспоненты")
        print(str(self.sco_exp(array_interpolation)) + " среднеквадратичное отклонение центральной производной экспоненты")

        # нахождение площадей
        print(str(self.sqrt_s_exp()) + " площадь 1 экспоненты")
        print(str(self.trap_s_exp()) + " площадь 2 экспоненты")
        print(str(self.simpsons_s_exp()) + " площадь 3 экспоненты")

        # графики
        figure, (axis1, axis2, axis3) = plt.subplots(1, 3)
        axis1.plot(array_x, array_difference_derivative_right)
        axis1.set_title("difference derivative right",  fontsize=7)
        axis1.grid()
        axis1.set_xlabel('X')
        axis1.set_ylabel('Y')

        # For difference derivative right Function
        axis2.plot(array_x, array_difference_derivative_left)
        axis2.set_title("difference derivative left",  fontsize=7)
        axis2.grid()
        axis2.set_xlabel('X')
        axis2.set_ylabel('Y')

        # For interpolation Function
        axis3.plot(array_x, array_interpolation)
        axis3.set_title("interpolation",  fontsize=7)
        axis3.grid()
        axis3.set_xlabel('X')
        axis3.set_ylabel('Y')

        plt.show()