# _*_ coding: utf8 _*_

puntos = [
	(1, 5),
	(2, 7),
	(-2, 4),
]

for p in puntos:
	x, y = p
	print "Punto: %dx %dy" % (x, y)

print "-" * 60

for x, y in puntos:
	print "Punto: %dx %dy" % (x, y)