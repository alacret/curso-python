# -*- coding: utf-8 -*-
'''
Python maneja 4 tipos de datos númericos:
- Enteros con signo (Integers o int)
- números largos o long
- numeros de punto flotante o float
- numeros complejos o complex (1i + j)
'''
# INT
a = 2
b = 2
c = a + b
print(c) # esperado: 4
a = 50
b = 5
c = 6
d = a - b*c
print(d)# esperado 20

# DIVISION:
a = 50
b = 5
c = 6
d = 4
e = (a - b*c) / d # Puedes usar parentesis para agrupar
print(e) # esperado 5.0
# NOTAS: las divisiones siempre devuelven float en python3

# ALGUNAS FUNCIONES
print(max(1,4,888)) #esperado 888

import math
print(math.ceil(1.1)) #esperado 2
print(math.floor(1.1)) #esperado 1

'''
- Funciones trigonometricas
- Numeros aleatorios
Referencia completa al modulo math:
https://docs.python.org/3/library/math.html
'''

'''
Ejercicios:
Abrir la referencia completa de math y probar algunas funciones

'''