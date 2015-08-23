class MiClase:
	'''
	Esta es la documentacion de mi clase,
	Esta clase esta diseñada solo para 
	pruebas, etc, etc
	'''
	def __init__(self):
		self.x = 2
		self._x = 3
		self.__x = 4
	def sumando(self, sumando):
		self.x += sumando
	

# Creando una instancia de la Clase
a = MiClase()
print(a.x)
print(a._x)
print(a.__x)

