import statistics

from matplotlib import pyplot as plt
import numpy as np
import math


class sin():
    def __init__(self):
        self.a = -np.pi
        self.b = np.pi
        self.h = 0.00001
        self.n = (self.b - self.a) / self.h
        self.array_phi = [self.a + self.h * i for i in np.arange(self.n)]
        self.phi = np.linspace(self.b, self.a, int(self.n) + 1) # шаги значение

    # Производные
    def difference_derivative_right(self):
        return [(np.sin(x + self.h) - np.sin(x)) / self.h for x in self.array_phi]

    def difference_derivative_left(self):
        return [(np.sin(x) - np.sin(x - self.h)) / self.h for x in self.array_phi]

    def difference_derivative_central(self):
        return [(np.sin(x + 1) - np.sin(x - 1)) / 2 * self.h for x in self.array_phi]

    # Среднеквадратичное значение
    def SKO(self, array, array_h):
        return math.sqrt((sum(x_i - mu for x_i, mu in zip(array, array_h)) ** 2) / self.n)

    # Площадь
    def Newton_Leibniz_formula(self):
        return [np.sin(self.a) - np.sin(self.a)]
    def rectangular_formula(self):
        return [sum((self.h * np.sin(x - 1)) for x in self.array_phi)]

    def trapezoid_formula(self):
        return [sum((self.h / 2 * (np.sin(x - 1) + np.sin(x))) for x in self.array_phi)]

    def simpsons_formula(self):
        return [sum((self.h / 4 * (np.sin(x - 1) + 4 * np.sin(x - 0.5) + np.sin(x))) for x in self.array_phi)]

    def func(self):
        array_h = self.array_phi

        # Производные от функции sin(x)

        # Правая разностная производная
        array_difference_derivative_right = self.difference_derivative_right()
        # Левая разностная производная
        array_difference_derivative_left = self.difference_derivative_left()
        # Центральная разностная производная
        array_difference_derivative_central = self.difference_derivative_central()

        # Среднеквадратичное отклонение

        print("Cреднеквадратичное отклонение правой разностной производной",self.SKO(array_difference_derivative_right, array_h))
        print("Cреднеквадратичное отклонение левой разностной производной", self.SKO(array_difference_derivative_left, array_h))
        print("Cреднеквадратичное отклонение центральной разностной производной", self.SKO(array_difference_derivative_central, array_h))

        # Площадь sin(x)

        print("Площадь sin(x) по формуле прямоугольников", self.rectangular_formula())
        print("Площадь sin(x) по формуле трапеция", self.trapezoid_formula())
        print("Площадь sin(x) по формуле Симпсона", self.simpsons_formula())
        print("Площадь sin(x) полученная аналитически с помощью формулы Ньютона Лейбница",self.Newton_Leibniz_formula())

        # график правой разностной производной
        figure, (axis1, axis2, axis3, axis4) = plt.subplots(1, 4)
        axis1.plot(self.array_phi, array_difference_derivative_right)
        axis1.set_title("difference derivative right", fontsize=7)
        axis1.grid()
        axis1.set_xlabel('X')
        axis1.set_ylabel('Y')

        # график левой разностной производной
        axis2.plot(self.array_phi, array_difference_derivative_left)
        axis2.set_title("difference derivative left", fontsize=7)
        axis2.grid()
        axis2.set_xlabel('X')
        axis2.set_ylabel('Y')

        # график центральной разностной производной
        axis3.plot(self.array_phi, array_difference_derivative_central)
        axis3.set_title("difference derivative central", fontsize=7)
        axis3.grid()
        axis3.set_xlabel('X')
        axis3.set_ylabel('Y')

        # ананалитический график
        axis4.plot(self.array_phi, self.phi * np.exp(self.phi))
        axis4.set_title("analytically", fontsize=7)
        axis4.grid()
        axis4.set_xlabel('X')
        axis4.set_ylabel('Y')
        plt.show()


        # графики зависимости
        arr_sko_right = []
        arr_sko_left = []
        arr_sko_center = []
        for x in self.phi[0:8]:
            arr_sko_right.append(self.SKO(array_difference_derivative_right, array_h))
            arr_sko_left.append(self.SKO(array_difference_derivative_left, array_h))
            arr_sko_center.append(self.SKO(array_difference_derivative_central, array_h))
            array_h = 2 * np.array(array_h)

        figure, (ax1, ax2, ax3) = plt.subplots(1, 3)

        ax1.plot(arr_sko_right, self.phi[0:8])
        axis3.set_title("difference derivative right SKO", fontsize=7)
        axis3.grid()
        axis3.set_xlabel('X')
        axis3.set_ylabel('Y')

        ax2.plot(arr_sko_left, self.phi[0:8])
        axis3.set_title("difference derivative left sko", fontsize=7)
        axis3.grid()
        axis3.set_xlabel('X')
        axis3.set_ylabel('Y')

        ax3.plot(arr_sko_center, self.phi[0:8])
        axis3.set_title("difference derivative central sko", fontsize=7)
        axis3.grid()
        axis3.set_xlabel('X')
        axis3.set_ylabel('Y')
        plt.show()