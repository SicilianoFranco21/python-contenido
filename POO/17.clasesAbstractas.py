"""
>>> CLASES ABSTRACTAS: Es una clase que no podemos instanciar pero funciona como molde o plantilla
                    para otras clases. Esto es util para no repetir codigo constantemente
                
    >>> EJEMPLO: Tenemos una clase llamada monstruo, que tiene atributos vida, maldad y un metodo ataque,
            podemos imaginar que es algo comun a todos los Monstruos, asi que creamos dos monstruos
            llamados monstruoDragon y monstruoOgro que heredan de la clase Monstruo las caracteristicas
            que todo monstruo deberia tener. Sumado a ello los monstruos creados a partir de Monstruo pueden
            tener sus propios metodos (Acciones) y caracteristicas (Propiedades)

            
    >>> Creacion de clase ABSTRACTA paso a paso: 
        1) PRIMERO:
            Debemos importar 'abc' para trabajar con clases abstractas  
                -> abc significa Abstract Base Class
                -> abstractmethod: Es un decorador que se coloca antes de un metodo
                            en una clase abstracta. Indica que el metodo es abstracto y que debe ser 
                            implementado por todas las clases concretas que hereden de la clase abstracta
                            - Utilizado para declararlo en la plantilla, se implementan en las clases concretas
                            - Una vez declarado el metodo abstracto hay que definirlo en la clase concreta obligatoriamente
                - Podemos hacerlo de la siguientes formas:
                [1] - from abc import ABC, abstractclassmethod
                [2] - from abc import *

        2) SEGUNDO:
            La clase abstracta debe heredar de ABC...
            -> class ClaseAbstracta(ABC):
        
        3) TERCERO:
            Crear un metodo abstracto con el decorador 'abstractclassmethod'
            -> @abstractclassmethod
    
    >>> VENTAJAS:
        1. EVITA COMPORTAMIENTOS ERRONEOS: Cuando una clase que hereda de la clase abstracta si o si necesita realizar "x" metodo, como "respirar"
            todas las clases concretas deben implementar dicho metodo SI o SI
        2. FOMENTA EL POLIMORFISMO: Todas las clases concretas tienen el mismo metodo (heredado de la clase abstracta) y por lo tanto
            puede ser utilizado por todas las clases concretas, responden a un mismo mensaje de manera similar (NO IGUAL)
        3. NIVEL EXTRA DE SEGURIDAD
        4. SE EVITA REPETIR CODIGO

"""

#Debemos importar 'abc' para trabajar con clases abstractas
from abc import ABC, abstractclassmethod


class Persona(ABC):
    @abstractclassmethod
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad
    
    @abstractclassmethod
    def hacer_actividad(self):
        pass
    
    #Aca no usamos metodo abstracto dado que esto es algo que todas las clases concretas tendran en COMUN
    def presentarse(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} anios")


class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad) #Hereda de la clase abstracta

    def hacer_actividad(self): #Implementamos hacer_actividad (metodo abstracto)
        print(f"Estoy estudiando {self.actividad}")


class Trabajador(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
    
    def hacer_actividad(self):
        print(f"Actualmente estoy trabajando en el rubro de {self.actividad}")
    

franco: Estudiante = Estudiante("Franco", 25, "Masculino", "programacion")
franco.presentarse() #llamamos al metodo comun a todas las clases 
franco.hacer_actividad() #llamamos al metodo abstracto, estudiante le da una implementacion puntual
print("\n")


trabajador_demberg: Trabajador = Trabajador("Demberg", 69, "Indefinido", "informatica")
trabajador_demberg.presentarse()
trabajador_demberg.hacer_actividad()