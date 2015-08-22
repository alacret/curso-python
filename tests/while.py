'''
print("INGRESA cinco numeros:\n\n\n")
c = 0
lista = []
while c < 5:
	entrada = input()
	lista.append(entrada)
	c = c + 1 # c += 1
	print(str(c) + " valores")

print("\n\n\n")
print(lista)
'''

















'''
while True:  # Para siempre
	num = input("QUIEN?: ")
	if num == 'x':
		break
	print("HOLA: ", num)

print("TERMINANDO")
'''










#Break y continue
a = 22
b = list(range(a))
for i in b:
	if i == 10 and 1 == True:
		continue
	print(i)
else:
	print("SE TERMINO EL CICLO")


	
