""" 
>>> EJERCICIO de Herencia Multiple y MRO: Modelar Zoologico

<<< REQUERIMIENTOS >>>
[1] -> Crear tres especies: Animal, Mamifero y Ave
[2] -> Animal puede comer, Mamifero puede amamantar, Ave puede volar
[3] -> Crear Murcielago, debe heredar caracteristicade de Mamifero y Ave (en este orden)
[4] -> (Opcional) Jugar con el orden de herencia de Murcielago asi vemos el MRO en accion 
"""

class Animal:
    def comer(self):
        print("El animal esta comiendo")


class Ave(Animal):
    def volar(self):
        print("El animal esta volando")


class Mamifero(Animal): 
    def amamantar(self):
        print("El animal esta amamantando")


class Murcielago(Ave, Mamifero):
    pass


murcielago = Murcielago()


murcielago.comer()
murcielago.volar()
murcielago.amamantar()


print(Murcielago.mro())
    