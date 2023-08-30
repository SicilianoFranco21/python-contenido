"""
>>> ACOMPLAMIENTO: Manera en la que se relacionan varios componentes entre ellos.
                ALTO ACOPLAMIENTO: Componentes muy relacionados entre si con muchas dependencias
                BAJO ACOPLAMIENTO: Componentes independientes unos respecto de otros

>>> Para que sirve? 
    Ejemplo para explicarlo: Estamos construyendo un juego de bloques con piezas que se encajan.
        Si haces que las piezas encajen muy fuerte, sera dificil cambiar una pieza sin afectar a todas
        las demas. Pero si las piezas tienen un leve contacto, se podra cambiar una pieza sin afectar
        a todo lo demas

>>> Ejemplo practico: Estamos haciendo un juego. Si el acomplamiento es alto, un cambio en una parte
    del juego puede afectar a muchas otras partes. Pero si el acoplamiento es bajo, podemos cambiar cosas
    sin causar problemas en otras partes

>>> El bajo acoplamiento se puede lograr aplicando buenas practicas, tales como los principios SOLID
"""


# Bajo Acoplamiento
# Notese la aplicacion del SRP, Motor tiene una unica responsabilidad y carro tambien
class Motor:
    def encender(self):
        print("Motor encendido")

class Carro:
    def __init__(self):
        self.motor = Motor()

    def arrancar(self):
        self.motor.encender()
        print("Carro arrancado")

carro = Carro()
carro.arrancar()


# Alto Acoplamiento
""" class Carro:
    def encender_motor(self):
        print("Motor encendido")

    def arrancar(self):
        self.encender_motor()
        print("Carro arrancado")

carro = Carro()
carro.arrancar() """