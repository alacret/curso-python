# -*- coding: utf-8 -*-

# Lists

lista = [1, 4, 9, 16, 25]
print(lista)

# Se puede acceder tambien por indice
print(lista[1])

# Tambien se puede hacer slice
print(lista[-3:])

# Concatenando con +
print(lista + [36, 49, 64, 81, 100])

# Reemplazando valores
lista[0] = "A"
print(lista)

lista[0:2] = ["A","L"]
print(lista)

lista.append("B")
lista.append("C")
lista.append("D")
print(lista)

# LISTA: Ref: https://docs.python.org/3/library/stdtypes.html?highlight=list#list


# Built in len()
print(len(lista))

# Lista bidimensionales
lista.append([2,2,2])
print(lista)

# List comprenhension: https://docs.python.org/2/tutorial/datastructures.html#list-comprehensions
# Operacones con lista y sus elementos

a = [3, 4, 5, 6, 7, 8]
# b = [i for i in a if i > 4]
print(b)
#
#b = filter(lambda x: x > 4, a)
# python3 filter devuelve un objeto iterable
print(b)
print(list(b))
print(b == b)
