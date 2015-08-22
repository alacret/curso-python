print ("Ingrese unos datos:")

lista = []
for i in range(5):
    num = input()
    lista.append(num)

print (lista)
print ("Ingrese un caracter: ")
variable = input()

if variable in lista:
    print ("Remover la posicion: \n")
    print (lista.index(variable))
    lista.remove(variable)
else:
    print ("El valor no se encuentra en la lista..")
print (lista)
