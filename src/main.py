class Animal:
    
    def __init__(self):
        print('ok')

    def comer(self): 
        print('animal comiendo...')

class Oso:

    def comer(self): 
        print('comiendo...')

class OsoPolar(Oso, Animal):

    def comer(self): 
        print('polar comiendo...')
        super().comer()
        Animal.comer(self)


def mostrarDatos(): 
    n = 234
    s = "asdf"
    print('-.....--------')


if __name__ == "__main__":
    n = OsoPolar()
    n.comer()
    mostrarDatos()