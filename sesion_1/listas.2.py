# _*_ coding: utf8 _*_

a = [5, 3, 8, 2, 1, 4, 1, 9, 6, 4, 2, 3]

menor = min(a)
mayor = max(a)

# index(x) - Devuelve el índice del primer elemento x encontrado

i_menor = a.index(menor)
i_mayor = a.index(mayor)

print "Menor %d (%d)" % (menor, i_menor)
print "Mayor %d (%d)" % (mayor, i_mayor)

print a