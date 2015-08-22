__author__ = 'alacret'

'''
ciclo FOR, para recorrer secuencias o tipos iterables

'''

for i in "python3":
    print(i)

l = ["uno", "dos", "tres"]

for i in l:
    print(i)

l = ("cuatro", "cinco", "seis")

for i in l:
    print(i)

# Python 3 enumerate: funcion para acarrear el indice de la iteracion

for i, v in enumerate(l):
    print(str(i) + ': ' + str(v))

# Los mapas se iteran de forma distinta
# Las claves:

m = {"uno":1, "dos":2, "tres":3}

for i in m.keys(): #Las claves
    print(i)

for i in m.values(): #Los valores
    print(i)

for k, v in m.items(): # Claves y valores
    print(str(k) + ': ' + str(v))