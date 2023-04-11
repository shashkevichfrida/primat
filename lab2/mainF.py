from matplotlib import pyplot as plt
import numpy as np
import math
import pandas as pd
from matplotlib.pyplot import figure
from matplotlib import mlab
import pylab
from methods.parabola import *
from methods.gold_section_search import *
from methods.brent import *



#метод золотого сечения
print("метод золотого сечения:")
print(gold_section_search(1, 5, 0.0001))


#парабола
print("метод параболы:")
print(parabola(1, 5, 0.0001))

#brent
print("метод брента:")
print(brent(1, 5, 0.001))


