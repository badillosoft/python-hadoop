# _*_ coding: utf-8 _*_

a = [1, 2, 5, 4, 6, 7, 3]
# b = [(1, "IMPAR"), (2, "PAR"), (5, "IMPAR"), ...]

def trans(x):
	if x % 2 == 0:
		return (x, "PAR")
	
	return (x, "IMPAR")

b = map(trans, a)

print b