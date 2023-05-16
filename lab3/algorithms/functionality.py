import numpy as np
from matplotlib import pyplot as plt


class functionality:
    stepFunc = 0

    def __init__(self, coefficients: np.array, tolerance: float):
        self.coefficients = coefficients
        self.tolerance = tolerance
        self.alpha = 0.01

    def func(self, A: np.array):
        summ = 0
        for i in range(self.coefficients.size):
            summ += self.coefficients[i] * A[i] ** 2

        return summ

    def funcWithStep(self, R: np.array, alpha, antiGrad: np.array):
        newR = np.zeros(R.size)
        for i in range(R.size):
            newR[i] = R[i] + alpha * antiGrad[i]
        return self.func(newR)

    def grad(self, R: np.array):
        r = np.zeros(R.size)
        for i in range(R.size):
            r[i] = 2 * self.coefficients[i] * R[i]

        return r

    def getDfDx(self, R: np.array):
        DF = self.grad(R)
        norm = np.linalg.norm(DF)
        for i in range(DF.size):
            DF[i] = -DF[i] / norm
        return DF

    def draw_func(self, a, b):
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1, projection='3d')
        x, y = np.mgrid[a:b:100j, a:b:100j]
        ax.contour(x, y, self.func(np.array(np.array([x,y]))), levels=20, colors='firebrick')
        plt.show()

    def draw(self, a, b, coordinates, title):
        fig, ax = plt.subplots()
        x, y = np.mgrid[a:b:100j, a:b:100j]
        ax.contour(x, y, self.func(np.array(np.array([x,y]))), levels=10, colors='firebrick')
        ax.set_title(title)
        for i in range(len(coordinates)):
            ax.scatter(coordinates[i][0], coordinates[i][1], c='black')
        ax.plot([coordinates[i][0] for i in range(len(coordinates))], [coordinates[i][1] for i in range(len(coordinates))], c='black')
        plt.show()
