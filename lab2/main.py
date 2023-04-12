from matplotlib import pyplot as plt
from methods.parabola import *
from methods.gold_section import *
from methods.brent import *
from methods.dichotomy import *
from methods.fibonacci import *

print("метод дихотомии:")
print(dichotomy(1, 5, 0.0001))


print("метод золотого сечения:")
print(gold_section(1, 5, 0.0001))


print("метод Фиббоначи:")
print(fibonacci(1, 5, 0.0001))


print("метод параболы:")
print(parabola(1, 5, 0.0001))


print("метод Брента:")
print(brent(1, 5, 0.0001))





fig, ax = plt.subplots()
ax.set_xlabel('x')
ax.set_ylabel('y')
x = np.linspace(-5, 5, 100)

y = np.sin(x) - np.log(x * x) - 1

min, f_min, iteration, call= dichotomy(1, 5, 0.0001)
ax.plot(min, f_min,'bo')

min, f_min, iteration, call= gold_section(1, 5, 0.0001)
ax.plot(min, f_min,'yo')

min, f_min, iteration, call= fibonacci(1, 5, 0.0001)
ax.plot(min, f_min,'go')

min, f_min, iteration, call= parabola(1, 5, 0.0001)
ax.plot(min, f_min,'bo')

min, f_min, iteration, call= brent(1, 5, 0.0001)
ax.plot(min, f_min,'ro')


ax.plot(x, y)
plt.show()