# _*_ coding: utf8 _*_

a = [1, 3, 5, 8, 9, 10, 13, 14, 15]

# append(x) - Añade el elemento x al final de la lista
# insert(i, x) - Añada el elemento x en la posición i

# remove(x) - Quita el primer elemento x de la lista
# pop(i) - Quita el elemento de la lista en la posición i

# count(x) - Cuenta el número de elementos iguales a x en la lista

a.pop(2) # [1, 3, 8, 9, ...]

a.insert(1, 4) # [1, 4, 3, 8, 9, ...]

if a.count(9) > 0:
	a.remove(9) # [1, 4, 3, 8, 10, ...]

a.append(18) # [1, 4, 8, 10, 13 14, 15, 18]

b = [1, 2, 3, 1, 1, 4, 2, 1, 2, 1]

# Quitar los los elementos iguales a 2

while b.count(2) > 0:
	b.remove(2)