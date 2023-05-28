from numpy.ma import array
from functionality import *
from algorithms.gradientConst import *
from algorithms.gradientCrushedSteps import *
from algorithms.gradientGoldenRation import *
from algorithms.gradientFibonacci import *

def main():
    e = dec(0.0001)
    x = array([dec(-1), dec(1)])
    draw_func(my_func, -1, 1)
    gradientConst(e, x)
    gradientCrushedSteps(e, x)
    gradientGoldenRation(e, x)
    gradientFibonacci(e, x)
    x = array([-4, 3])
    '''A = array([[2, 1],
         [1, 4]])
    b = array([0, 0])'''
    '''A = array([[2, 0],
               [0, 2]])
    b = array([-1, 0])
    conjugate_gradient(x, A, b, e)'''


main()