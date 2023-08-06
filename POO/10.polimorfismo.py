"""
>>> POLIMORFISMO: Capacidad de un objeto para comportarse de diferentes maneras, segun
            el contexto en el que se use. Esto significa que un objeto puede cambiar su comportamiento cuando
            se le llama de una forma u otra
            - Se da mismo mensaje, distinto comportamiento!
            - POLIMORFISMO = "Muchas formas"

            
>>> EJEMPLO:
class Animal:
    def hacer_sonido(self):
        print("Ruido desconocido")

class Perro(Animal):
    def hacer_sonido(self):
        print("Guau guau")

class Gato(Animal):
    def hacer_sonido(self):
        print("Miau miau")

class Pajaro(Animal):
    def hacer_sonido(self):
        print("Pío pío")

Observaciones: Le damos el MISMO MENSAJE a cada animal, y cada uno se COMPORTA DISTINTO
"""

# >>> Polimorfismo con OBJETOS
class Gato:
    def sonido(self):
        return "Miau"


class Perro:
    def sonido(self):
        return "Guau"
    

gato: Gato = Gato()
perro: Perro = Perro()


print(gato.sonido())
print(perro.sonido())


# >>> Polimorfismo con OBJETOS + Funciones (Polimorfismo de funcion)
def hacer_ruido(animal):
    print(animal.sonido())


hacer_ruido(gato)
hacer_ruido(perro)