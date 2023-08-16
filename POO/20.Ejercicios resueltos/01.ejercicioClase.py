"""
Crea una clase llamada Persona que tenga atributos como nombre y edad. 
Luego, crea objetos de esta clase y muestra sus atributos.
"""
#RECOMENDACION: Expresar libertad creativa en el ejercicio. No descuidar el desenfoque del mismo y que funcione correctamente


#Crear la clase Persona
class Persona:
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad


#Generar instancias de la clase Persona
persona1: Persona = Persona("Agustina", 24)
persona2: Persona = Persona("Santino", 18)


#Funcion para mostrar los atributos de las instancias creadas a partir de la clase Persona
def presentarse(*args: Persona) -> None:
    contador_personas: int = 0
    for persona in args:
        contador_personas += 1
        print(f"[{contador_personas}] --> Hola me llamo {persona.nombre} y mi tengo {persona.edad} anios")


#Llamar al PROCEDIMIENTO 'presentarse' (Aca esta mi libertad creativa respecto a como mostrar los atributos)
presentarse(persona1, persona2)