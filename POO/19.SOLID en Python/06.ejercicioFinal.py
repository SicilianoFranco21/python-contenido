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
import os


class PersonajeGenerico(ABC):
    def __init__(self, nombre, vida, stamina, ataque, defensa):
        self.nombre = nombre
        self.vida = vida
        self.stamina = stamina
        self.ataque = ataque
        self.defensa = defensa
    
    @abstractmethod
    def atacar(self, enemigo):
        danio: int = self.ataque - enemigo.defensa
        if danio > 0:
            print(f"El {self.__class__.__name__} {self.nombre} ha daniado a el {enemigo.__class__.__name__} {enemigo.nombre} por {danio} puntos")
        else:
            print(f"El {self.__class__.__name__} {self.nombre} no consiguio lastimar a {enemigo.__class__.__name__} {enemigo.nombre}")
    
    @abstractmethod
    def descansar(self, recuperacion_vida, recuperacion_stamina):
        self.vida += recuperacion_vida
        self.stamina += recuperacion_stamina
        print(f"{self.__class__.__name__} {self.nombre} ha recuperado -> +{recuperacion_vida} puntos de vida | +{recuperacion_stamina} puntos de stamina")


class Guerrero(PersonajeGenerico):
    def __init__(self, nombre, vida, stamina, ataque, defensa):
        super().__init__(nombre, vida, stamina, ataque, defensa)
    
    def atacar(self, enemigo):
        super().atacar(enemigo)
        self.stamina -= 10
        
    def descansar(self):
        recuperacion_vida: int = int((self.vida*25)/100)
        recuperacion_stamina: int = int((self.stamina*25)/100)
        super().descansar(recuperacion_vida, recuperacion_stamina)


class Gladiador(PersonajeGenerico):
    def __init__(self, nombre, vida, stamina, ataque, defensa):
        super().__init__(nombre, vida, stamina, ataque, defensa)

    def atacar(self, enemigo):
        super().atacar(enemigo)
        self.stamina -= 25

    def descansar(self):
        recuperacion_vida: int = int((self.vida*25)/100)
        recuperacion_stamina: int = int((self.stamina*50)/100)
        super().descansar(recuperacion_vida, recuperacion_stamina)


class Juego:
    @classmethod
    def ganar_juego():
        pass
    
    @classmethod
    def jugar(cls, personajes: list):
        cantidad_jugadores: int = len(personajes)
        turno: int = 1
        jugando: bool = True
        while jugando:
            index_jugador_actual: int = (turno - 1)%cantidad_jugadores
            jugador_actual = personajes[index_jugador_actual]
            comando: str = input("1. Atacar\n2. Descansar\n3. Pasar turno\nIngresar un comando: ")
            if comando == "1":
                pass
            elif comando == "2":
                jugador_actual.descansar()
            elif comando == "3":
                pass
            else:
                pass
                #print("Vuelva a intentarlo por favor")
                #comando: str = input("1. Atacar\n2. Descansar\n3. Pasar turno\nIngresar un comando: ")
            turno += 1
            print(turno)


guerrero = Guerrero("Manowar", 100, 120, 15, 10)
gladiador = Gladiador("Gladius", 100, 100, 15, 20)

guerrero.atacar(gladiador)
print()
gladiador.atacar(guerrero)
print()
guerrero.descansar()
print()
gladiador.descansar()

Juego.jugar([guerrero, gladiador])