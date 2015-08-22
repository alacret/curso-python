# -*- coding: utf-8 -*-

# Comilla simple
a = 'hola'
print(a)

a = "hola" # Comillas dobles
print(a)

a = "\"hola\""  # backslash para escapar
print(a)

a = '"hola", fue lo que dijo'  # Se pueden combinar
print(a)

a = '"hola",\n fue lo que dijo'  # Incluyendo caracteres especiales
print(a)

# Usando multiples lineas
a = '''
Hola,
Fue lo que dijo
Multiples lineas
'''
print(a)

a = (''
'Hola,'
'Fue lo que dijo'
     )
print(a)

# CONCATENANDO con el operador +
a = "Hola, mi nombre es: "
b = "Angel Lacret "
print(a + b)

print("Hola, mi nombre es: " + "Angel Lacret ")

# REPITIENDO con el operador *
a = 3
b = "Angel Lacret "
print(a * b)

# Un string se puede acceder por indice
a = "Angel Lacret "
print(a[1])

# Algunas funciones
print(len(a))
print(a.capitalize())
print(a.find('n'))
print(a.isalpha())

# https://docs.python.org/3/library/stdtypes.html?highlight=str#str

# Formatting (https://docs.python.org/3/library/string.html#formatstrings)
a = "Mi nombre es: {0}"
print(a.format("Angel Lacret"))

a = '{0}, {1}, {2}'.format('a', 'b', 'c')
print(a)
a = '{}, {}, {}'.format('a', 'b', 'c')  # 3.1+ only
print(a)
a = '{2}, {1}, {0}'.format('a', 'b', 'c')
print(a)
a = '{2}, {1}, {0}'.format(*'abc')      # unpacking argument sequence
print(a)
a = '{0}{1}{0}'.format('abra', 'cad')   # arguments' indices can be repeated
print(a)

'''
UNICODE: https://docs.python.org/release/3.0.1/howto/unicode.html
'''