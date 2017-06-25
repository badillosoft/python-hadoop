# _*_ coding: utf8 _*_

def min_max(lista):
	return (min(lista), max(lista))

a, b = min_max([1, 8, 3, 0, 5, 4, 6, 2, 3])

print "Mínimo: %d" % (a)
print "Máximo: %d" % (b)