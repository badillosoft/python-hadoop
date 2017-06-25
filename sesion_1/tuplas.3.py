# _*_ coding: utf8 _*_

X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Y = [10, 1, 4, 5, 8, 6, 4, 5, 2]

Z = zip(X, Y)

for x, y in Z:
	print "Punto: %dx %dy" % (x, y)

W = zip(X, Y, Z)

print W