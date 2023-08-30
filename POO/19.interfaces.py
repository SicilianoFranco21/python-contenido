"""
>>> INTERFAZ: Contrato que establece que cosas debe hacer una clase sin preocuparse
    por como las hace.
    ACLARACION: Python como tal no tiene interfaces, pero las podemos representar con clases abstractas
    
>>> POR QUE USARLAS?
    -> Define que funciones (metodos) debe tener una clase, pero no proporciona su implementacion especifica
    -> Ayuda a organizar y estructurar el codigo de manera mas clara y flexible
    > Al usar interfaces, se garantiza que las clases que implementan esa interfaz cumplan con un contrato especifico

>>> VENTAJAS
    -> Flexibilidad: Las clases pueden implementar varias interfaces, lo que permite la combinacion de comportamientos diferentes en una clase
    -> Mantenimiento: Cambiar la implementacion de una interfaz no afectara el codigo que utiliza esa interfaz, siempre y cuando el contrato se mantenga
    -> Reusabilidad: Reutilizar codigo en diferentes partes de la aplicacion sin preocuparte por la implementacion subyacente (detalles internos, etc)

>>> EJEMPLO GENERICO
from abc import ABC, abstractmethod


# "Interfaz" implementada mediante clases abstractas
class MiInterfaz(ABC):
    @abstractmethod
    def metodo_abstracto(self):
        pass

class MiClase(MiInterfaz):
    def metodo_abstracto(self):
        print("Implementación del método en MiClase")


class OtraClase(MiInterfaz):
    def metodo_abstracto(self):
        print("Implementación del método en OtraClase")


# Esto es posible debido a la implementación de interfaces
def usar_interfaz(objeto):
    objeto.metodo_abstracto()


# Instanciamos las clases
objeto1 = MiClase()
objeto2 = OtraClase()

usar_interfaz(objeto1)
usar_interfaz(objeto2)

"""


from abc import ABC, abstractmethod


# Implementar Interfaz
class Personaje(ABC):
    def __init__(self, nombre, vida, resistencia, ataque, defensa):
        self.nombre: str = nombre
        self.vida: int = vida
        self.resistencia: int = resistencia
        self.ataque: int = ataque
        self.defensa: int = defensa

    # Se definen como implementar dos metodos abstractos con el fin de que las clases hijas lo hereden y luego agreguen sus extensiones a dichos metodos
    @abstractmethod
    def atacar(self, enemigo, desgaste):
        danio: int = self.ataque - enemigo.defensa
        if self.resistencia > 0:
            if danio > 0:
                self.resistencia -= desgaste
                enemigo.vida -= danio
                print(f"{enemigo.nombre} ha perdido {danio} puntos de vida")
            else:
                print(f"{enemigo.nombre} no ha perdido puntos de vida")
    
    @abstractmethod
    def descansar(self, recuperacion):
        self.resistencia += recuperacion

    # Metodo especial, al no ser utilizado el decorador @abstractmethod no es necesario implementarlo en las clases hijas
    def __str__(self):
        return f"{self.nombre} es un {__class__.__name__}"


# Usar Interfaz para crear a nuestros personajes
class Guerrero(Personaje):
    def __init__(self, nombre, vida, resistencia, ataque, defensa):
        super().__init__(nombre, vida, resistencia, ataque, defensa)
        
    def atacar(self, enemigo):
        print(f"{self.nombre} usa: Corte del leviatan!")
        desgaste: int = 20
        super().atacar(enemigo, desgaste)
    
    def descansar(self):
        recuperacion: int = 30
        super().descansar(recuperacion)
        print(f"{self.nombre} recupera la resistencia, ahora tiene {self.resistencia} puntos de resistencia")


# Usar Interfaz para crear a personajes de otro tipo
class Mago(Personaje):
    def __init__(self, nombre, vida, resistencia, ataque, defensa, mana):
        super().__init__(nombre, vida, resistencia, ataque, defensa)
        self.mana: int = mana
    
    def atacar(self, enemigo):
        print(f"{self.nombre} usa: Juicio Final!")
        desgaste: int = 15
        super().atacar(enemigo, desgaste)
    
    def descansar(self):
        recuperacion: int = 20
        super().descansar(recuperacion)
        print(f"{self.nombre} recupera la resistencia, ahora tiene {self.resistencia} puntos de resistencia")
        

guerrero = Guerrero("G Bryce", 100, 180, 15, 10)
guerrero2 = Guerrero("G Gladius", 100, 100, 20, 10)
guerrero.atacar(guerrero2)
guerrero.descansar()

print("""
----------------------------------------------------------------------
""")

mago = Mago("M Bryce", 100, 100, 15, 10, 200)
mago2 = Mago("M Gladius", 100, 100, 20, 10, 200)
mago.atacar(mago2)
mago.descansar()