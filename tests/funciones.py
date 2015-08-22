def imprimir_nombre(nombre):
	n = str(nombre)
	print("HOLA " + n)

def hola(nombre="John Doe", multiplicador=7):
	if multiplicador > 5:
		imprimir_nombre(nombre)
		print("Demasiados nombres")
		return nombre
	
	for i in range(multiplicador):
		imprimir_nombre(nombre)

	return nombre




def exponencial(base, e):
	'''
	Una funcion que eleva una base
	al exponente
	'''
	if e == 0:
		return None
	r = 1
	for i in range(e):
		r = r * base
	return r

















def ultimo(lista):
    valor = ""
    for i in lista:
        valor = i
    return valor













