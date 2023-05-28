from math import fabs, sqrt

from functionality import dec, my_func, draw

h = dec(0.000001)

goldenRat = (1.0 + sqrt(5)) / 2.0


def goldSection(point, a, b, eps, h):
    x, y = point[0], point[1]
    grad_x = (my_func(x + h, y) - my_func(x - h, y)) / (2 * h)
    grad_y = (my_func(x, y + h) - my_func(x, y - h)) / (2 * h)

    x1 = a + (b - a) / (dec(goldenRat) + 1)
    x2 = b - (b - a) / (dec(goldenRat) + 1)
    f_1 = my_func(x - grad_x * x1, y - grad_y * x1)
    f_2 = my_func(x - grad_x * x2, y - grad_y * x2)
    while fabs(b - a) > eps:
        if f_1 >= f_2:
            a = x1
            x1 = x2
            x2 = b - (b - a) / (dec(goldenRat) + 1)
            f_1 = f_2
            f_2 = my_func(x - grad_x * x2, y - grad_y * x2)
        else:
            b = x2
            x2 = x1
            x1 = a + (b - a) / (dec(goldenRat) + 1)
            f_2 = f_1
            f_1 = my_func(x - grad_x * x1, y - grad_y * x1)
    return (a + b) / 2


def gradientGoldenRation(eps, point):
    next_point = point.copy()
    count = 0
    points_x = []
    points_y = []
    while True:
        count = count + 1
        points_x.append(next_point[0])
        points_y.append(next_point[1])
        f = my_func(point[0], point[1])
        grad_x = (my_func(point[0] + h, point[1]) - my_func(point[0] - h, point[1])) / (2 * h)
        grad_y = (my_func(point[0], point[1] + h) - my_func(point[0], point[1] - h)) / (2 * h)
        gold_ratio = goldSection(point, dec(-8), dec(8), eps, h)
        next_point[0] = point[0] - gold_ratio * grad_x
        next_point[1] = point[1] - gold_ratio * grad_y
        f_next = my_func(next_point[0], next_point[1])
        if fabs(point[0] - next_point[0]) <= eps and fabs(point[1] - next_point[1]) <= eps and fabs(f - f_next) <= eps:
            break
        point = next_point.copy()
    draw(-2, 2, my_func, points_x, points_y, 'Gradient with Golden ration method')
    print('gradient_descent_golden:', 'func_value = ', my_func(point[0], point[1]), 'x = ', point[0], ' y = ', point[1], 'iterations =  ', count)
