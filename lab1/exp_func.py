from matplotlib import pyplot as plt
import numpy as np
import math

class exp():
    def __init__(self):
        self.a = -4
        self.b = 4
        self.h = 0.00001
        self.n = (self.b - self.a) / self.h
        self.array_phi = [self.a + self.h * i for i in np.arange(self.n)]
        self.phi = np.linspace(self.a, self.b, int(self.n) + 1)

    # Производные
    def difference_derivative_right(self):
        return [(np.exp(x + self.h) - np.exp(x)) / self.h for x in self.array_phi]
    def difference_derivative_left(self):
        return [(np.exp(x) - np.exp(x - self.h)) / self.h for x in self.array_phi]

    def difference_derivative_central(self):
        return [(np.exp(x + 1) - np.exp(x - 1)) / 2 * self.h for x in self.array_phi]

    def real_difference(self):
        return [(x * np.exp(x) for x in self.array_phi)]

    # Среднеквадратичное значение
    def SKO(self, array):
        sco = 0
        average_value = sum(array) / len(array)
        for x in np.arange(len(array)):
            sco = sco + math.sqrt((1 / (len(array) - 1))) * (array[x] - average_value) ** 2
        return sco

    # Площадь
    def rectangular_formula(self):
        return [sum((self.h * np.sin(x - 1)) for x in self.array_phi)]

    def trapezoid_formula(self):
        return [sum((self.h / 2 * (np.sin(x - 1) + np.sin(x))) for x in self.array_phi)]

    def simpsons_formula(self):
        return [sum((self.h / 4 * (np.sin(x - 1) + 4 * np.sin(x - 0.5) + np.sin(x))) for x in self.array_phi)]



    def func(self):

        # Производные от функции sin(x)

        # Правая разностная производная
        array_difference_derivative_right = self.difference_derivative_right()
        # Левая разностная производная
        array_difference_derivative_left = self.difference_derivative_left()
        # Центральная разностная производная
        array_difference_derivative_central = self.difference_derivative_central()
        # Релаьные значения провзводной
        array_real_values = self.real_difference()


        # Среднеквадратичное отклонение

        print("Cреднеквадратичное отклонение правой разностной производной", self.SKO(array_difference_derivative_right))
        print("Cреднеквадратичное отклонение левой разностной производной", self.SKO(array_difference_derivative_left))
        print("Cреднеквадратичное отклонение центральной разностной производной", self.SKO(array_difference_derivative_central))

       # Площадь exp(x)

        print("Площадь exp(x) по формуле прямоугольников", self.rectangular_formula())
        print("Площадь exp(x) по формуле трапеция", self.trapezoid_formula())
        print("Площадь exp(x) по формуле Симпсона", self.simpsons_formula())

        # график правой разностной производной
        figure, (axis1, axis2, axis3, axis4) = plt.subplots(1, 4)
        axis1.plot(self.array_phi, array_difference_derivative_right)
        axis1.set_title("difference derivative right",  fontsize=7)
        axis1.grid()
        axis1.set_xlabel('X')
        axis1.set_ylabel('Y')

        # график левой разностной производной
        axis2.plot(self.array_phi, array_difference_derivative_left)
        axis2.set_title("difference derivative left",  fontsize=7)
        axis2.grid()
        axis2.set_xlabel('X')
        axis2.set_ylabel('Y')


        # график центральной разностной производной
        axis3.plot(self.array_phi, array_difference_derivative_central)
        axis3.set_title("difference derivative central",  fontsize=7)
        axis3.grid()
        axis3.set_xlabel('X')
        axis3.set_ylabel('Y')

        # ананалитический график
        axis4.plot(self.array_phi,  self.phi * np.exp(self.phi))
        axis4.set_title("analytically", fontsize=7)
        axis4.grid()
        axis4.set_xlabel('X')
        axis4.set_ylabel('Y')


        plt.show()
