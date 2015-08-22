__author__ = 'alacret'

'''
ciclo WHILE, para iterar mientras se cumple
alguna condicion, o mientras una condicion
es verdadera

'''

c = 0
while c < 9:
   print('La cuenta es: ', c)
   c += 1

'''
Leyendo entrada por teclado
'''

while True:  # Para siempre
    num = input("QUIEN?: ")
    if num == 'x':
        break
    print("HOLA: ", num)

'''
 Tanto el FOR como el WHILE pueden contener un ELSE,
 que se ejecuta al final del conteo en caso del FOR,
 y al evaluar FALSE en caso del WHILE
'''

while False:
    print("NUNCA POR AQUI")
else:
    print("SIEMPRE POR AQUI")


'''
Dentro del ciclo se pueden usar las sentencia   s:
- break: para salir del ciclo
- continue: para saltar a la siguiente evaluacion de la condicion
- pass: que no hace nada
'''

c = 0
while c < 9:
    print('La cuenta es:', c)
    if c == 3:
        break
    c += 1

'''
Llenar un lista con cinco entradas de teclado,
luego iterarlo hasta encontrar un caracter especial


Contar en que posicion esta el caracter especial

'''