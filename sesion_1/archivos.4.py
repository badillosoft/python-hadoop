# _*_ coding: utf-8 _*_

f = open("datos.txt", "r")

puntos = []

for linea in f:
	xs, ys = linea.split(" ")
	x = float(xs)
	y = float(ys)
	puntos.append((x, y))

f.close()

X, Y = zip(*puntos)

print X
print Y