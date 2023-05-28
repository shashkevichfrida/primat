from math import fabs

from functionality import dec, my_func, draw

h = dec(0.000001)


def gradientConst(eps, point):
    next_point = point.copy()
    count = 0
    points_x = []
    points_y = []
    e = dec(0.01)
    while True:
        count += + 1
        points_x.append(next_point[0])
        points_y.append(next_point[1])
        f = my_func(point[0], point[1])
        grad_x = (my_func(point[0] + h, point[1]) - my_func(point[0] - h, point[1])) / (2 * h)
        grad_y = (my_func(point[0], point[1] + h) - my_func(point[0], point[1] - h)) / (2 * h)
        next_point[0] = point[0] - e * grad_x
        next_point[1] = point[1] - e * grad_y
        f_next = my_func(next_point[0], next_point[1])
        if fabs(point[0] - next_point[0]) <= eps and fabs(point[1] - next_point[1]) <= eps and fabs(f - f_next) <= eps:
            break
        point = next_point.copy()
    draw(-2, 2, my_func, points_x, points_y, 'Gradient with constant method')
    print('gradient_descent_const', 'func_value = ', my_func(point[0], point[1]), 'x = ', point[0], ' y = ', point[1], 'iterations =  ', count)
