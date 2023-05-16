import numpy as np
import algorithms.functionality as fc
import algorithms.dihotomyStep as dS
import algorithms.gradientDescent as gD
import algorithms.standartStep as sS
import algorithms.armijoStep as aS
import algorithms.conjugateGrad as cG


arr = np.array([2,3])
coeff = np.array([10,20])
functional = fc.functionality(coeff, 0.05)
# print(functional.grad(arr))

func = fc.functionality(coeff, 0.1)
func.stepFunc = dS.dihotomyStep2
coord = gD.Decent(arr, func)
#pprint(np.matrix(coord))

func.draw_func(-5, 5)

func.draw(-5, 5, coord, "fast")

func.stepFunc = sS.standartStep
coord1 = gD.Decent(arr, func)
#pprint(np.matrix(coord))
func.draw(-5, 5, coord1, "standart")

func.stepFunc = aS.armijoStep
coord2 = gD.Decent(arr, func)
#pprint(np.matrix(coord))
func.draw(-5, 5, coord2, "armijo")

coord3 = cG.conjugate_grad(arr, func)
func.draw(-5, 5, coord3, "conjugate")