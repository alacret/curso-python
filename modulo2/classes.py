__author__ = 'alacret'

'''
Las clases en python son un tipo de dato
'''

# Asi basicamente

class MiClase:
    pass


a = MiClase() #Instanciar la clase
print(a)
a.x = 2 # Las instancias son dianmicas, se pueden modifcar en RUNTIME
print(a.x)

'''
 Constructores, metodos y variables
 El constructor y los metodos se definen igual que una funcion, ademas
  de las siguientes reglas:
 - El constructor y los metodos de instancia tienen un primer parametro
 obligatorio con el nombre especial de SELF
 - Los metodos estaticos o de clase tienen que estar decorados con @STATICMETHOD o @CLASSMETHOD
'''

class MiClase:
    '''
    MI DOCUMENTACION
    '''
    c = 1  # Variables estaticas o de la clase

    def __init__(self):
        self.x = 2  # self para las variables de instancias

    def sumar(self, a):
        self.x += a

    @staticmethod
    def otra_constante():
        return 3.14

# Las clases tambien son tipos de datos y tienen variables y metodos
print(MiClase.c)
print(MiClase.otra_constante())

a = MiClase() #Instanciar la clase
print(a.x)
a.sumar(3)
print(a.x)

'''
Variables o metodos privados
A difencia de otros lenguajes OO, python no incluye la posiblidad de metodos o variables privadas
Pero, por convencion se usa el underscore (_) para metodos o variables de uso interno de las clases
o modulos, que solo intervienen en ese contexto y que no estan diseñados para exponerse

'''

# HERENCIA


class MiClase:
    '''
    MI DOCUMENTACION
    '''
    def __init__(self):
        self.x = 2  # self para las variables de instancias

    def sumar(self, a):
        self.x += a


class MiSubClase(MiClase):
    '''
    MI DOCUMENTACION de Sub clase
    '''
    pass

a = MiSubClase()
a.sumar(2)
print(a.x)

# Herencia Multiple


class MiClase:
    '''
    MI DOCUMENTACION
    '''
    def __init__(self):
        self.x = 2  # self para las variables de instancias

    def sumar(self, a):
        self.x += a


class MiOtraClase:
    '''
    MI DOCUMENTACION
    '''
    def __init__(self):
        self.x = 4  # self para las variables de instancias

    def sumar(self, a):
        self.x += a


class MiSubClase(MiClase, MiOtraClase):
    '''
    MI DOCUMENTACION de Sub clase
    '''
    pass


class MiOtraSubClase(MiOtraClase, MiClase):
    '''
    MI DOCUMENTACION de Sub clase
    '''
    pass

a = MiSubClase()
a.sumar(2)
print(a.x)

b = MiOtraSubClase()
b.sumar(2)
print(b.x)