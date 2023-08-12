"""  
>>> DIP: Los modulos de alto nivel (scope mas amplio y generico) NO deben depender de los modulos de bajo nivel (Componentes mas concretos que cumplen funciones especializadas)
        Ambos deben depender de abstracciones, y a su vez, estas no deben depender de los detalles, sino que los detalles deben depender de las abstracciones
        -> En lugar de que un modulo dependa directamente de otro modulo, ambos modulos deben depender de interfaces o abstracciones
            comunes. 
        
        >>> EJEMPLO 1: Tenemos que crear autos de motores electricos y a gasolina, para este caso
                    nos conviene crear una clase abstracta (o interfaz) llamada EngineInterface con el proposito de
                    poder crear otras dos clases, llamadas ElectricEngine y GasolineEngine, estas dependen de la interfaz (clase abstracta)
                    creada anteriormente
            
                from abc import ABC, abstractmethod

                # Definimos la interfaz para los motores
                class EngineInterface(ABC):
                    @abstractmethod
                    def start(self):
                        pass

                # Implementación de un motor de gasolina
                class GasolineEngine(EngineInterface):
                    def start(self):
                        print("Gasoline Engine started")

                # Implementación de un motor eléctrico
                class ElectricEngine(EngineInterface):
                    def start(self):
                        print("Electric Engine started")

                # Clase de carro que usa un motor
                class Car:
                    def __init__(self, engine: EngineInterface):
                        self.engine = engine
                    
                    def start(self):
                        self.engine.start()

                # Crear instancias de motores
                gasoline_engine = GasolineEngine()
                electric_engine = ElectricEngine()

                # Crear carros con diferentes motores
                car1 = Car(gasoline_engine)
                car2 = Car(electric_engine)

                # Iniciar los carros (sin importar el tipo de motor)
                car1.start()
                car2.start()
        
        ------------------------------------------------------------

        >>> EJEMPLO 2: Juego de rol (RPG), aplicamos el DIP a una interfaz 'Character', que contiene metodos 'attack' y 'defend'.
                    Luego, creamos diferentes tipos de personajes, 'Warrior' y 'Wizzard', que implementaran la interfaz 'Character'.
                    El sistem de combate de alto nivel dependera de la interfaz 'Character' y no de las implementaciones
                    especificas como 'Warrior' y 'Wizzard', esto permite agregar nuevos tipos de personajes sin cambiar la logica
                    de combate existente
"""


from abc import ABC, abstractmethod


# Definición de la interfaz para los personajes
class Character(ABC):
    @abstractmethod
    def attack(self):
        pass
    
    @abstractmethod
    def defend(self):
        pass


# Implementación del guerrero
class Warrior(Character):
    def attack(self):
        print("Warrior attacks with a sword")
    
    def defend(self):
        print("Warrior raises shield for defense")


# Implementación del mago
class Wizard(Character):
    def attack(self):
        print("Wizard casts a fireball spell")
    
    def defend(self):
        print("Wizard raises a magical barrier for defense")


# Procedimiento que simula un combate
def simulate_combat(character):
    print("\nEntering combat:")
    character.attack()
    character.defend()


# Crear instancias de personajes
warrior = Warrior()
wizard = Wizard()


# Simular combates con diferentes personajes
simulate_combat(warrior)
simulate_combat(wizard)