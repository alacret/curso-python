# -*- coding: utf-8 -*-
'''
Las tuplas son una secuencias de datos, valores u objetos,
similares a las listas o arreglos en otros lenguajes.
En python las tuplas son inmutables (no se pueden actualizar)
'''

# Sus valores se separan por comas
t = "uno", 2, "tres", 4;
print(t)

# Si quieres crear una tupla con un solo elemento debes usar la como al final
t = "uno",;
print(t)

# Si quieres crear una tupla vacia debes usar los parentesis
t = ();
print(t)
print(t is None)

# Se acceden por indice, y aplican las operaciones de slice
t = "uno", 2, "tres", 4;
print(t[1])
print(t[1:])

# Por ser inmutable toda operacion sobre una tupla devuelve un objeto nuevo
# Tambien, es imposible actualizarlas

# ERROR: t[0] = 1;

# Operaciones con + y *
t = "uno", 2,;
print(t + ("tres", 4));
print(t * 2);

# Tambien se pueden anidar
t = 1, (2,2,2,2), (3, "tres"), (-4,4);
print(t)

# algunas funciones
print(len(t))