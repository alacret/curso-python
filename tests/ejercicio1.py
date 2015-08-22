a = 0
lista=[]

while a < 5:
    value=input("Ingrese un valor")
    lista.append(value)
    a+=1

search = input("Ingrese un valor a buscar")

for i in lista:
    if i == search:
        print(lista.index(search))
        lista.remove(search)
        print(lista)
