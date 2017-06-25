# _*_ coding: utf8 _*_

a = [5, 3, 8, 2, 1, 4, 1, 9, 6, 4, 2, 3]

# Baby Algorithm for sort numbers

# Repite n veces: (n - tamaño de la lista)
# 1. Busca el menor de la lista
# 2. Quita al menor
# 3. Agregalo a nueva lista

n = len(a)

b = []

for i in range(n):
	x = min(a)
	a.remove(x)
	b.append(x)

print b