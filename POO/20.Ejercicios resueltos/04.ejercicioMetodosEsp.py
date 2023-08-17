"""
Crea una clase Punto que represente un punto en un plano 2D.
Implementa el método __str__ para imprimir el punto de manera legible.
"""
# RECOMENDACION: Expresar libertad creativa en el ejercicio. No descuidar el enfoque del mismo y que funcione correctamente


class Punto:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x}; {self.y})"


punto1: Punto = Punto(3, 4.5)
punto2: Punto = Punto(-2, 3)


print(punto1, punto2)