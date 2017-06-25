# _*_ coding: utf8 _*_

# Generar los primeros 100 números de Fibonacci

a = [1, 1]

for i in range(98):
	a.append(a[-1] + a[-2])

print a