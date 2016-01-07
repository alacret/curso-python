class Test():
	def __init__(self):
		self.__p = 1
	def _private(self):
		print(self.__p)

class SubTest(Test):
	def __init__(self):
		self.__private()

print(Test()._private())
