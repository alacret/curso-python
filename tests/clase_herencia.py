class persona:
	def __init__(self, nombre = "Nadie"):
		self.nombre = nombre
	def printer(self):
		print(self.nombre)

class PersonaNatural(persona):
	def cedula(self, cedula=None):
		if cedula is None:
			print(cedula)
		else:
			self.micedula = cedula
	def printer(self):
		cedula = str(self.micedula)
		t = self.nombre+":"+cedula
		print(t)


class PersonaJuridica(persona, PersonaNatural):
	def __init__(self, nombre, rif=None):
		self.nombre = nombre
		self.rif(rif)
	def rif(self,rif=None):
		if rif is None:
			print (rif)
		else:
			self.mirif= rif
			
	def printer(self):
		rif = str(self.mirif)
		t = self.nombre + ":" +rif
		print(t)

a = PersonaNatural("Daniela")
a.cedula(21233233)
a.printer()
b = PersonaJuridica("4GEEKS MCBO C.A.")
b.rif("J-4IUIUIUIU")
b.printer()
persona_j = PersonaJuridica("PAPELERIA RAMI","J2")
persona_j.printer()



