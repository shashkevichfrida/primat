from algorithms.gradientDescentConstStep import *
from algorithms.conjugateGradients import *

if __name__ == '__main__':
    #градиентный спуск с постоянным шагом
    gradient_desc_const_step()

    A = np.array([[4, -1], [-1, 3]])
    b = np.array([2, 1])
    x0 = np.array([0, 0])

    #сопряженные градиенты
    conjugate_gradient(A, b, x0)

