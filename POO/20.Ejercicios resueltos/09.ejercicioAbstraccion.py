"""
Crea una clase abstracta FiguraGeometrica con un método
abstracto calcular_area(). Luego, crea subclases como 
Circulo y Rectangulo que implementen este método.
"""
# RECOMENDACION: Expresar libertad creativa en el ejercicio. No descuidar el enfoque del mismo y que funcione correctamente


from abc import ABC, abstractclassmethod, abstractmethod


class FiguraGeometrica(ABC):
    @abstractclassmethod
    def calcular_area():
        pass
    

class Circulo(FiguraGeometrica):
    def calcular_area(r: float, pi: float = 3.14):
        return pi*(r**2)
    

class Rectangulo(FiguraGeometrica):
    def calcular_area(base: float, altura: float):
        return base*altura


print("Area circulo:", Circulo.calcular_area(4))
print("Area rectangulo:", Rectangulo.calcular_area(3, 4))