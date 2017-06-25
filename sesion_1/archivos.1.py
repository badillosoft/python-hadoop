# _*_ coding: utf-8 _*_

f = open("fibo.txt", "w")

a = 1
b = 1

f.write("1 1 ")

n = 2

for i in range(20 - 2):
	c = a + b
	f.write("%d " % (c))
	
	a = b
	b = c
	n += 1

	if n % 5 == 0:
		f.write("\n")

f.close()