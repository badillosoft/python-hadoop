# _*_ coding: utf-8 _*_

a = [1, 2, 3, 4, 5]
# b = [(1, 1), (2, 4), (3, 9), ...]

b = map(lambda x: (x, x ** 2), a)

print b