# _*_ coding: utf-8 _*_

import math
import numpy as np
import matplotlib.pyplot as plt

def f(x):
	return 2. / (1. + math.exp(-x * 0.05)) - 1.0

X = np.linspace(-100, 100, 100)
Y = [f(x) for x in X]

plt.plot(X, Y, "r--")

plt.show()