"""
Crea una clase Punto que represente un punto en un plano 2D.
Implementa el método __str__ para imprimir el punto de manera legible.
"""
# RECOMENDACION: Expresar libertad creativa en el ejercicio. No descuidar el enfoque del mismo y que funcione correctamente


# Crear clase Punto
class Punto:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    
    def __str__(self): # Utilizar met. esp. __str__ (recordar: cuando se realiza print no devolvera un codigo, devolvera lo indicado en el return)
        return f"({self.x}; {self.y})"


# Crear instancias de la clase Punto
punto1: Punto = Punto(3, 4.5)
punto2: Punto = Punto(-2, 3)


# Aca podremos apreciar el resultado del metodo esp. __str__
print(punto1, punto2)