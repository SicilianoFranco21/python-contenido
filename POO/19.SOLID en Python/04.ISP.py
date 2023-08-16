"""
>>> ISP: Muchas interfaces especificas del cliente son mejores que una interfaz de
        proposito general. Ningun cliente tiene que ser forzado a depender de interfaces que no necesite, es decir,
        eliminar las dependencias que no vamos a utilizar

        >>> EJEMPLO: Estamos creando un juego de monstruos, donde cada monstruo puede atacar,
                    moverse y volar. Sin aplicar el ISP tendriamos una clase GRANDE llamada monstruo
                    que hace todo lo siguiente:

                    OBSERVACION: Todos los monstruos realizan estas 3 acciones
                                incluso si hay monstruos que no puedan volar
                                    class Monstruo:
                                        def atacar(self):
                                            # Código para el ataque

                                        def moverse(self):
                                            # Código para moverse

                                        def volar(self):
                                            # Código para volar

                    * En cambio, APLICANDO el ISP dividimos las cosas en partes mas pequenias y especificas:
                            class Atacante:
                                def atacar(self):
                                    # Código para el ataque

                            class Caminante:
                                def moverse(self):
                                    # Código para moverse

                            class Volador:
                                def volar(self):
                                    # Código para volar
                    
                    * Finalmente, para cada tipo de monstruo usariamos solo las partes que necesita:
                            class MonstruoTerrestre(Atacante, Caminante):
                                pass

                            class MonstruoAereo(Atacante, Volador):
                                pass

                            class MonstruoNadador(Atacante):
                                pass                        
"""


from abc import ABC, abstractmethod

# Las clases Trabajador, Comedor y Durmiente cada una tiene un metodo abstracto con el proposito de aplicar ISP
class Trabajador(ABC):
    @abstractmethod
    def trabajar(self):
        pass


class Comedor(ABC):
    @abstractmethod
    def comer(self):
        pass


class Durmiente(ABC):
    @abstractmethod
    def dormir(self):
        pass


# Tanto la clase Robot como Humano heredan lo que necesitan para caracterizarse
class Humano(Trabajador, Comedor, Durmiente):
    def comer(self):
        print("El humano esta comiendo")

    def trabajar(self):
        print("El humano esta trabajando")

    def dormir(self):
        print("El humano esta durmiendo")


class Robot(Trabajador):
    def trabajar(self):
        print("El Robot esta trabajando")


robot: Robot = Robot()
humano: Humano = Humano()


print("ROBOT")
robot.trabajar()

print("\nHUMANO")
humano.comer()
humano.trabajar()
humano.dormir()
