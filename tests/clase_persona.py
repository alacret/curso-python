class persona ():
	def __init__(self, name="N", lastname="A"):
		self.name = name
		self.lastname = lastname
	def nombre(self,name):
		self.name = name
	def last(self,lastname):
		self.lastname = lastname
	def printer(self):
		print(self.name + " " + 
			self.lastname)
	 	
a = persona("Daniela", "Nieto")
a.printer()
a.nombre("Nestor")
a.printer()
b = persona("Yendry", "Viloria")
b.printer()

variable = persona()
variable.printer()



