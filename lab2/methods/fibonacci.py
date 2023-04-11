import numpy as np

def f(x):
    return np.sin(x) - np.log(x * x) - 1

def fibonacci_sequence(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a


def fibonacci(left, right, epsilon):
    array = []
    iteration = 0
    call = 0

    n = 1
    while fibonacci_sequence(n + 2) <= (right - left) / epsilon:
        n += 1

    a = left
    b = right

    x1 = a + fibonacci_sequence(n) / fibonacci_sequence(n + 2) * (b - a)
    x2 = a + fibonacci_sequence(n + 1) / fibonacci_sequence(n + 2) * (b - a)

    f1 = f(x1)
    f2 = f(x2)


    while b - a > epsilon and a < b:
        iteration += 1
        if (f1 > f2):
            n -= 1
            a = x1
            x1 = x2
            x2 = a + fibonacci_sequence(n + 1) / fibonacci_sequence(n + 2) * (b - a)
            f1 = f2
            f2 = f(x2)
        else:
            n -= 1
            b = x2
            x2 = x1
            x1 = a + fibonacci_sequence(n) / fibonacci_sequence(n + 2) * (b - a)
            f2 = f1
            f1 = f(x1)
        call += 1
    middle = (a + b) / 2
    return middle, f(middle), call, iteration, array