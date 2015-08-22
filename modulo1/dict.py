# -*- coding: utf-8 -*-

'''
DICCIONARION (PROGRAMACION)
Un vector asociativo (también contenedor asociativo, mapa, mapeador, hash, diccionario,
mapa finito, tabla de consulta) es un tipo abstracto de dato formado por una colección
de claves únicas y una colección de valores, con una asociación uno a uno

Las claves de los diccionarios deben ser tipos de datos inmutables: Strings, numeros o tuplas

Se definen con llaves, y se acceden con corchetes
'''

zoo = {"leon": 2, "tigre": 6}
print(zoo)
print(zoo["leon"])

d = {1: 2, 2: 6}
print(d)

# errOR: print(d[9])

'''
Las claves son unicas pero los valores se pueden repetir
'''

d = {1: 2, 2: 6, 1:8, 3:6}
print(d)

# añadiendo valores nuevos
d[4] = 78
print(d)

# actualizando valores
d[1] = "uno"
print(d)

# borrando valores
del d[2]
print(d)

# algunas funciones

# lista de claves
animales = zoo.keys()
print(list(animales))

#lista de valores
cantidades = zoo.values()
print(list(cantidades))

# lista de tuplas clave, valor
zoo_tuplas = zoo.items()
print(list(zoo_tuplas))

#NOTA: PYTHON 3 devuelve views para ciertos iterables

'''
EJERCICIO: Construir un diccionario que represente una casa, y que posea atributos como:
- numero de cuartos, numero de ventandas, tamaño
entonces: crear varias casas
'''