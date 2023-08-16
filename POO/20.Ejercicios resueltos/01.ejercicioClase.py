"""
Crea una clase llamada Persona que tenga atributos como nombre y edad. 
Luego, crea objetos de esta clase y muestra sus atributos.
"""


class Persona:
    def __init__(self, nombre, edad):
        self.nombre: str = nombre
        self.edad: int = edad


persona1: Persona = Persona("Agustina", 24)
persona2: Persona = Persona("Santino", 18)


def presentarse(*args: Persona) -> None:
    contador_personas: int = 0
    for persona in args:
        contador_personas += 1
        print(f"[{contador_personas}] --> Hola me llamo {persona.nombre} y mi tengo {persona.edad} anios")


presentarse(persona1, persona2)