from matplotlib import pyplot as plt
import numpy as np
import math
import pandas as pd
from matplotlib.pyplot import figure
from matplotlib import mlab
import pylab
from methods.parabola import *
from methods.gold_section import *
from methods.brent import *
from methods.dichotomy import *
from methods.fibonacci import *

print("метод дихотомии:")
print(dichotomy(1, 5, 0.0001))


print("метод золотого сечения:")
print(gold_section_search(1, 5, 0.0001))


print("метод Фиббоначи:")
print(fibonacci(1, 5, 0.0001))


print("метод параболы:")
print(parabola(1, 5, 0.0001))


print("метод брента:")
print(brent(1, 5, 0.0001))


