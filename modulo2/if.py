__author__ = 'alacret'

'''
Condicionales de flujo: IF

Similar a la mayoria de lenguajes de programacion

'''

a = True

if a == True:
    print("Sentencia condicionada")

if a: # Python autmaticamente evalua en los if
    print("Sentecnia condicionada mas simple")

if a is not False: # Sintaxis de python
    print("Sentecnia condicionada con la expresion IS NOT")

if a is not None: # Sintaxis de python, evaluando identidad, siempre con IS
    print("Sentecnia condicionada con el objeto NONE")

# ELSE

if a is False:
    print("NUNCA LO VOY A IMPRIMIR")
else:
    print("Probando el else")

# ELIF

if a is False:
    print("NUNCA LO VOY A IMPRIMIR")
elif a is True:
    print("Probando el elif")

'''
python no tiene switch

'''

'''
Ejercicio:

- Imprimir 1 o 2 en funcion de una variable booleana

- Actualizar un diccionario con un valor, evaluando una variable
'''