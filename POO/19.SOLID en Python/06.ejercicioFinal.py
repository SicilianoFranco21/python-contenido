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


# Funciona como "interfaz" para crear personajes mas especificos, en este caso Guerrero y Mago
class PersonajeGenerico(ABC):
    def __init__(self, nombre, vida, stamina, ataque, defensa):
        self.nombre = nombre
        self.vida = vida
        self.stamina = stamina
        self.ataque = ataque
        self.defensa = defensa
    
    # atacar() y descansar() son metodos abstractos que son comunes a todas las clases hijas que hereden de PersonajeGenerico
    @abstractmethod
    def atacar(self, enemigo):
        danio: int = self.ataque - enemigo.defensa
        if danio > 0:
            print(f"El {self.__class__.__name__} {self.nombre} ha daniado a el {enemigo.__class__.__name__} {enemigo.nombre} por {danio} puntos")
            enemigo.vida -= danio
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
    
    # Hereda se la clase padre el metodo atacar + se le agrega una extension del funcionamiento de dicho metodo
    def atacar(self, enemigo):
        super().atacar(enemigo)
        self.stamina -= 10
    
    # Hereda se la clase padre el metodo descansar + se le agrega una extension del funcionamiento de dicho metodo
    def descansar(self):
        recuperacion_vida: int = int((self.vida*25)/100) #Formula para obtener el porcentaje de un numero -> (numero*porcentaje_a_obtener)/100
        recuperacion_stamina: int = int((self.stamina*25)/100)
        super().descansar(recuperacion_vida, recuperacion_stamina)

    # Cada vez que imprimamos a la instancia de la clase aparecera lo indicado en el return
    def __str__(self):
        return f"{self.__class__.__name__} {self.nombre}"


class Gladiador(PersonajeGenerico):
    def __init__(self, nombre, vida, stamina, ataque, defensa):
        super().__init__(nombre, vida, stamina, ataque, defensa)

    # Hereda se la clase padre el metodo atacar + se le agrega una extension del funcionamiento de dicho metodo
    def atacar(self, enemigo):
        super().atacar(enemigo)
        self.stamina -= 25

    # Hereda se la clase padre el metodo descansar + se le agrega una extension del funcionamiento de dicho metodo
    def descansar(self):
        recuperacion_vida: int = int((self.vida*25)/100) #Formula para obtener el porcentaje de un numero -> (numero*porcentaje_a_obtener)/100
        recuperacion_stamina: int = int((self.stamina*50)/100)
        super().descansar(recuperacion_vida, recuperacion_stamina)

    # Cada vez que imprimamos a la instancia de la clase aparecera lo indicado en el return
    def __str__(self):
        return f"{self.__class__.__name__} {self.nombre}"


# Clase encargada de ejecutar el juego
class Juego:
    @classmethod
    def obtener_jugadores_vivos(cls, jugadores_vivos: list):
        for jugador in jugadores_vivos:
            if jugador.vida <= 0:
                jugadores_vivos.remove(jugador)
    
    @classmethod
    def determinar_ganador(cls, cantidad_jugadores_vivos: int, jugadores_vivos: list):
        jugando: bool = True
        if cantidad_jugadores_vivos == 1:
            print(f"El ganador es {jugadores_vivos[0]}")
            jugando = False
        return jugando
    
    @classmethod
    def validar_opciones(cls, cantidad_opciones: int, mensaje: str):
        opcion: int = int(input(f"Ingresar {mensaje}: "))
        while opcion < 1 or opcion > cantidad_opciones:
            opcion: int = int(input(f"Intentelo nuevamente, ingresar {mensaje}: "))
        return opcion
    
    @classmethod
    def seleccionar_objetivo(cls, cantidad_jugadores, jugadores):
        index_objetivo: int = cls.validar_opciones(cantidad_jugadores, mensaje="objetivo a atacar") - 1
        objetivo = jugadores[index_objetivo]
        return objetivo
        
    @classmethod
    def jugar(cls, jugadores: list):
        cantidad_jugadores: int = len(jugadores)
        jugadores_vivos: list = jugadores.copy() #Copia de jugadores con el proposito de usarla como lista auxiliar y no romper el programa por modificar la "fuente de datos" original
        turno: int = 1
        jugando: bool = True
        
        while jugando:
            index_jugador_actual: int = (turno - 1)%cantidad_jugadores
            jugador_actual = jugadores[index_jugador_actual]
            print(f"\n>>> Turno {turno}\n>>> Le toca a {jugador_actual}\n")
            
            # Bloque de codigo encargado de ejecutar un comando introducido por el usuario
            print("1. Atacar\n2. Descansar\n3. Pasar turno")
            OPCIONES_COMBATE: int = 3
            comando: int = cls.validar_opciones(OPCIONES_COMBATE, mensaje="comando")
            if comando == 1:
                os.system("cls")
                objetivo = cls.seleccionar_objetivo(cantidad_jugadores, jugadores)
                jugador_actual.atacar(objetivo)
            elif comando == 2:
                os.system("cls")
                jugador_actual.descansar()
            elif comando == 3:
                os.system("cls")
                print(f"{jugador_actual.nombre} decide pasar su turno")
            
            # Este bloque de codigo evalua cual es el jugador que queda en pie
            cls.obtener_jugadores_vivos(jugadores_vivos)
            cantidad_jugadores_vivos: int = len(jugadores_vivos)
            jugando: bool = cls.determinar_ganador(cantidad_jugadores_vivos, jugadores_vivos)
            
            turno += 1


# Crear instancias de clases concretas 
guerrero = Guerrero("Manowar", 100, 120, 100, 15)
gladiador = Gladiador("Gladius", 100, 100, 15, 20)

# Ejecutar el metodo de clase jugar() de la clase Juego
Juego.jugar([guerrero, gladiador])


