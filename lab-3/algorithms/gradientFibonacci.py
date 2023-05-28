from math import fabs

from functionality import dec, my_func, draw

h = dec(0.000001)

def fib(n):
    f1 = 1
    f2 = 1
    m = 0
    while m < n - 1:
        f = f1 + f2
        f1 = f2
        f2 = f
        m = m + 1
    return f1

def fibonacci(point, a, b, eps, h):
    x, y = point[0], point[1]
    k = 0
    n = 0
    fn1 = 1
    fn2 = 1
    dell = (b - a) / eps
    while fn1 < dell:
        fn = fn1 + fn2
        fn1 = fn2
        fn2 = fn
        n = n + 1
    x1 = a + dec(fib(n) / fib(n + 2)) * (b - a)
    x2 = a + dec(fib(n + 1) / fib(n + 2)) * (b - a)
    grad_x = (my_func(x + h, y) - my_func(x - h, y)) / (2 * h)
    grad_y = (my_func(x, y + h) - my_func(x, y - h)) / (2 * h)
    y1 = my_func(x - grad_x * x1, y - grad_y * x1)
    y2 = my_func(x - grad_x * x2, y - grad_y * x2)
    while fabs(b - a) > eps:
        k = k + 1
        if y1 >= y2:
            a = x1
            x1 = x2
            y1 = y2
            x2 = a + dec(fib(n - k + 2) / fib(n - k + 3)) * (b - a)
            y2 = my_func(x - grad_x * x2, y - grad_y * x2)
        else:
            b = x2
            x2 = x1
            y2 = y1
            x1 = a + dec(fib(n - k + 1) / fib(n - k + 3)) * (b - a)
            y1 = my_func(x - grad_x * x1, y - grad_y * x1)
    _x = (a + b) / 2
    return _x

def gradientFibonacci(eps, point):
    next_point = point.copy()
    count = 0
    points_x = []
    points_y = []
    while True:
        count = count + 1
        f = my_func(point[0], point[1])
        points_x.append(next_point[0])
        points_y.append(next_point[1])
        fib = fibonacci(point, dec(-8), dec(8), eps, h)
        grad_x = (my_func(point[0] + h, point[1]) - my_func(point[0] - h, point[1])) / (2 * h)
        grad_y = (my_func(point[0], point[1] + h) - my_func(point[0], point[1] - h)) / (2 * h)
        next_point[0] = point[0] - fib * grad_x
        next_point[1] = point[1] - fib * grad_y
        f_next = my_func(next_point[0], next_point[1])
        if fabs(point[0] - next_point[0]) <= eps and fabs(point[1] - next_point[1]) <= eps and fabs(f - f_next) <= eps:
            break
        point = next_point.copy()
    draw(-2, 2, my_func, points_x, points_y, 'Gradient with Fibonacci method')
    print('gradient_descent_fibonacci:', 'func_value = ', my_func(point[0], point[1]), 'x = ', point[0], ' y = ', point[1], 'iterations =  ', count)


