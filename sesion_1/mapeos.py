# _*_ coding: utf-8 _*_

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# b = [1, 4, 9, 25, 36, 49, 64, 81]

def al_cuadrado(x):
	return x ** 2

b = map(al_cuadrado, a)

print b