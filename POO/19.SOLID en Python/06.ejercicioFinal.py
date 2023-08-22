"""
EJERCICIO con el proposito de aplicar la mayor cantidad de conceptos posibles de POO
(Sin descuidar los principios S.O.L.I.D)

>>> CREAR UN JUEGO DE RPG (Jugable desde consola unicamente)

    -> Descripcion: El jugador se sumerge en un mundo medieval lleno de magia, criaturas misteriosas
                    y tesoros ocultos. 
                    El objetivo principal del juego es enfrentarse a enemigos y reunir los 7 tesoros que 
                    contienen pegarminos con poder magico para aumentar las habilidades de los personajes + monedas de oro
    -> Requerimientos:
                    -> Personajes: 
                            - Guerrero, puede atacar con espada y defenderse con escudo (Sin mana)
                            - Mago, Lanza bolas de fuego y crea barreras magicas para defenderse (Con mana)
                            - Paladin, puede atacar con la espada y defenderse con barreras magicas (Mitad de mana que el mago)
                            - Herrero, es el que fabrica las armaduras para los demas personajes (Sin mana) 
                    -> Mecanicas del juego:
                            - Cada personaje tiene una barra de salud (HP), energia (stamina) y habilidades unicas (libertad creativa, aunque el Herrero si o si su habilidad unica es la herreria)
                            - Los tesoros aumentan las stats de los personajes + monedas de oro
                            - Crear un menu con opciones para: Empezar a jugar, elegir clase y nombre de nuestro personaje de cabecera,
                                seleccionar cantidad de enemigos y salir del juego
    -> Criterios de aceptacion:  
                    - Cada personaje debe poder realizar las habilidades especificadas en los requerimientos
                    - Las status comunes a todos los personajes luchadores son ataque, defensa y HP
                    - Los herreros tienen HP y pueden crear espadas, armaduras y escudos
                    - Los tesoros se otorgaran al ganador de cada ronda
                    - La cantidad de rondas sera igual a la cantidad de personajes introducidos (sin contar nuestro personaje)
                    - Cada opcion del menu principal debe realizar lo indicado en la seccion "Mecanicas del juego"
                    - Finalizacion del juego: El juego finaliza cuando el jugador gana a todos los personajes o pierde una sola vez
                    - Si el juegador pierde, se borraran los datos del mismo
                    - Si el jugador gana, su personaje se mantendra guardado
"""


from abc import ABC, abstractmethod, abstractclassmethod


class Juego:
    turno_actual: int = 0
    turno_jugador: int = 0
    
    @classmethod
    def seleccionar_jugador(cls, personajes: list):
        cantidad_jugadores: int = len(personajes)
        if (cls.turno_jugador == cantidad_jugadores - 1):
            cls.turno_jugador = 0
        elif (cls.turno_jugador < cantidad_jugadores) and (cls.turno_actual != 0):
            cls.turno_jugador += 1
        print("\nselector jugador:", cls.turno_jugador, "\n")
        return cls.turno_jugador
    
    @classmethod
    def jugar(cls, personajes: list):
        jugando: bool = True
        while jugando:
            personaje_actual: int = personajes[cls.seleccionar_jugador(personajes)]
            print("\nTurno:", cls.turno_actual + 1, f"Le toca a {personaje_actual.__class__.__name__}")
            comando: str = input("1. Atacar\n2. Defender\n3. Ataque Especial\nIngresar una opcion: ")
            if comando == "1":
                atacar_a = int(input(f"\nSeleccionar personaje (seleccionando un numero del 1 al {len(personajes)}): "))
                atacar_a -= 1
                personaje_actual.atacar(personajes[atacar_a])
            elif comando == "2":
                pass
            elif comando == "3":
                pass
            cls.turno_actual += 1
            


class AtributosMagicos:
    def __init__(self, mana):
        self.mana = mana


class PersonajeGenerico(ABC):
    def __init__(self, hp, stamina, ataque, defensa):
        self.hp = hp
        self.stamina = stamina
        self.ataque = ataque
        self.defensa = defensa


class PersonajeMagico(PersonajeGenerico, AtributosMagicos):
    def __init__(self, hp, stamina, ataque, defensa, mana):
        PersonajeGenerico.__init__(self, hp, stamina, ataque, defensa)
        AtributosMagicos.__init__(self, mana)


class InterfazCombate(ABC):
    @abstractmethod
    def habilidad_especial(self):
        pass
    
    @abstractmethod
    def atacar(self, enemigo):
        danio: int = self.ataque - enemigo.defensa
        if danio > 0:
            print(f"{enemigo.__class__.__name__} ha recibido {danio} puntos de danio")
            enemigo.hp -= danio
        else:
            print(f"{enemigo.__class__.__name__} no ha recibido danio")
        self.stamina -= 10
    
    @abstractmethod
    def defender(self, enemigo):
        danio: int = enemigo.ataque - self.defensa
        if danio > 0:
            print(f"{self.__class__.__name__} perdio {danio} puntos de vida por el ataque de {enemigo.__class__.__name__}. ")
            self.hp -= danio
        else:
            print(f"El ataque de {enemigo.__class__.__name__} no tuvo efecto en {self.__class__.__name__}")
        self.stamina -= 5


class Guerrero(PersonajeGenerico, InterfazCombate):
    def __init__(self):
        super().__init__(hp=100, stamina=100, ataque=35, defensa=30)

    def habilidad_especial(self, enemigo):
        ataque_especial: int = int(self.ataque*2)
        danio: int = ataque_especial - enemigo.defensa
        print("Mandoble: Tajo decreciente")
        if danio > 0:
            print(f"{enemigo.__class__.__name__} ha recibido {danio} puntos de danio")
            enemigo.hp -= danio
        else:
            print(f"{enemigo.__class__.__name__} no ha recibido danio")
        self.stamina -= 25
        
    def atacar(self, enemigo):
        super().atacar(enemigo)

    
    def defender(self, enemigo):
        super().defender(enemigo)


class Mago(PersonajeMagico, InterfazCombate):
    def __init__(self):
        super().__init__(hp=200, stamina=60, ataque=15, defensa=10, mana=200)

    def habilidad_especial(self, enemigo):
        print("Hechizo: esferas de fuego. (Produce fatiga al enemigo)")
        ataque_especial: int = int(self.ataque*1.5)
        danio: int = ataque_especial - enemigo.defensa
        enemigo.stamina -= int((enemigo.stamina*20)/100)
        if danio > 0:
            print(f"{enemigo.__class__.__name__} ha recibido {danio} puntos de danio")
            enemigo.hp -= danio
            print(enemigo.hp)
        else:
            print(f"{enemigo.__class__.__name__} no ha recibido danio")
        self.stamina -= 10

    def atacar(self, enemigo):
        super().atacar(enemigo)

    
    def defender(self, enemigo):
        super().defender(enemigo)


class Paladin(PersonajeMagico, InterfazCombate):
    def __init__(self):
        super().__init__(hp=120, stamina=80, ataque=25, defensa=20, mana=100)

    def habilidad_especial(self, enemigo):
        print("Fuerzas celestiales")
        ataque_especial: int = int(self.ataque*1.75)
        danio: int = ataque_especial - enemigo.defensa
        self.hp += int(self.hp*25/100)
        if danio > 0:
            print(f"{enemigo.__class__.__name__} ha recibido {danio} puntos de danio")
            enemigo.hp -= danio
        else:
            print(f"{enemigo.__class__.__name__} no ha recibido danio")
        self.stamina -= 20

    def atacar(self, enemigo):
        super().atacar(enemigo)

    
    def defender(self, enemigo):
        super().defender(enemigo)


class Herrero(PersonajeGenerico):
    def __init__(self):
        super().__init__(hp=50, stamina=200, ataque=5, defensa=5)

    def habilidad_especial(self):
        print("Herrería")


herrero = Herrero()
print(f"HP: {herrero.hp} | Stamina: {herrero.stamina} | Ataque: {herrero.ataque} | Defensa: {herrero.defensa}")
""" herrero.habilidad_especial() """
print()


paladin = Paladin()
print(f"HP: {paladin.hp} | Stamina: {paladin.stamina} | Ataque: {paladin.ataque} | Defensa: {paladin.defensa} | Mana: {paladin.mana}")
""" paladin.habilidad_especial() """
print()


mago = Mago()
print(f"HP: {mago.hp} | Stamina: {mago.stamina} | Ataque: {mago.ataque} | Defensa: {mago.defensa} | Mana: {mago.mana}")
""" mago.habilidad_especial() """
print()


guerrero = Guerrero()
print(f"HP: {guerrero.hp} | Stamina: {guerrero.stamina} | Ataque: {guerrero.ataque} | Defensa: {guerrero.defensa}")
""" guerrero.habilidad_especial() """

print()
mago.habilidad_especial(guerrero)
print()
""" guerrero.atacar(mago)
paladin.defender(guerrero) """
paladin.habilidad_especial(mago)
print()
guerrero.habilidad_especial(paladin)
print()

Juego.jugar([guerrero, mago, paladin])