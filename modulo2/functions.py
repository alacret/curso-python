__author__ = 'alacret'

'''
En python, una funcion es un bloque de codigo reutilizable,
con una definicion, que puede ser utilizado en cualquier
otro lugar del programa.

Esta definicion incluye los parametros que recibe,
opcionales o no, y el cuerpo de la funcion y cero
o cualquier cantidad de sentencias return.

En python, las funciones tambien son un tipo de datos,
es decir, puede asignarse a una variable, operarse, e
incluso pasarse como parametro a otra funcion
'''


def hola():
    print("HOLA MUNDO") # una funcion que no devuelve
    # nada, devuelve None
    return None

hola()
hola()








# Siempre es bueno documentar tus funciones
def hola():
    "Una funcion que dice hola"
    print("HOLA MUNDO") # una funcion que no devuelve nada, devuelve None

print(hola.__doc__)


# Parametros

def hola(quien):
    "Una funcion que le dice hola a alguien"
    print("HOLA ", quien)

hola("ANGEL")
hola("JOSE")

'''
Parametros opcionales o por defecto, son parametros
a los que se le puede asignar un valor en caso de que
no sean pasados al llamar la funcion
'''


def hola(quien="John Doe"):
    "Una funcion que le dice hola a alguien o a nadie"
    print("HOLA ", quien)

hola("ANGEL")
hola()

# Tambien podemos devolver valores


def cuadrado(a):
    "Calcula el cuadrado de un valor"
    b = a * a
    return b

c = cuadrado(2)
print(c)

c = cuadrado(2) + cuadrado(3)
print(c)

# una funcion puede devolver cualquier tipo de dato

def cuadrado(a):
    "Calcula el cuadrado de un valor"
    b = a * a
    return a, b

a = 2
d, c = cuadrado(a)
print(a == d)
print(c)

# Multiple return

def cuadrado(a):
    "Calcula el cuadrado de un valor"
    if a == 0:
        return 0, 0
    b = a * a
    return a, b

a, b = cuadrado(0)
print(a)

# Dentro de las funciones las variables son locales y no afectan las que estan fuera de ella

def cuadrado(c):
    "Calcula el cuadrado de un valor"
    if c == 0:
        return 0, 0
    b = c * c
    a = 99999999999999
    return c, b

a = 2
b, c = cuadrado(a)
print(a)

# a menos que usamos la sentencia GLOBAL

def cuadrado(c):
    "Calcula el cuadrado de un valor"
    global a
    if c == 0:
        return 0, 0
    b = c * c
    a = 99999999999999
    return c, b

a = 2
b, c = cuadrado(a)
print(a)

#  parametros indefinidos

def cuadrado(*valores):
    "Calcula el cuadrado de una lista de valores"
    originales = valores
    cuadrados = []
    for i in valores:
        cuadrados.append(i * i)
    return list(originales), cuadrados

a = 2
b, c = cuadrado(a,2,3,4,1)
print(b,c)

'''
Ejercicios

1)Dado una lista o tupla, devolver en una funcion
el ultimo elemento, ejemplo:
[1,2,1,1,1,2,2,2,3,3,4,4,4,1]
devuelve 1

2) Cuenta las donas: imprime una frase que indica
la cantidad de donas. La entrada es el numero de
donas que se tiene, sin embargo, si el numero es
mas grande que diez, imprima el string DEMASIADAS donas

3) Un programa que imprime el cuadrado del
numero ingresado
'''