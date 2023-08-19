"""
Crea una jerarquía de clases que representen diferentes
instrumentos musicales, como guitarras y pianos. Cada instrumento 
puede tener un método tocar() que imprima un mensaje. Luego,
crea una función que tome una lista de instrumentos y haga que
cada uno sea tocado.
"""
# RECOMENDACION: Expresar libertad creativa en el ejercicio. No descuidar el enfoque del mismo y que funcione correctamente


# Utilizaremos una clase padre abstracta con el proposito de obligar al programador a definir el metodo tocar si o si
from abc import ABC, abstractclassmethod, abstractmethod


# Crear clase generica instrumento
class Instrumento(ABC):
    @abstractmethod
    def tocar(self):
        pass


# Crear sub-clases que heredan de instrumento
class Guitarra(Instrumento):
    def tocar(self):
        print("La guitarra esta sonando")


class Piano(Instrumento):
    def tocar(self):
        print("El piano esta sonando")


class Violin(Instrumento):
    def tocar(self):
        print("El violin esta sonando")
        

instrumentos: list = [Guitarra(), Piano(), Violin(), Guitarra()]


# Definir procedimiento para tocar todos los instrumentos
def tocar_instrumento(instrumentos: list) -> None:
    for instrumento in instrumentos:
        instrumento.tocar()
    

# Ejecutar procedimiento    
tocar_instrumento(instrumentos)