# _*_ coding: utf-8 _*_

import math
import numpy as np
import matplotlib.pyplot as plt

def f(x):
	return 2. / (1. + math.exp(-x * 0.5)) - 1.0

X = np.linspace(-1, 1, 100)
Y = [f(x) for x in X]

a = open("datos.txt", "w")

for x, y in zip(X, Y):
	a.write("%.8f %.8f\n" % (x, y))

a.close()