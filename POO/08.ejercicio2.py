"""

EJERCICIO de herencia y uso de super: Crear un sistema para una escuela

>>> Requerimientos:
[1]. ENTIDADES: 
Persona: 
    - Nombre
    - Edad
    - metodo -> Imprimir nombre y edad de la persona
 
Estudiante:
    - Hereda de persona
    - Grado
    - metodo -> Imprimir grado del estudiante

[2]. Crear instancia de la clase Estudiante
[3]. Imprimir sus atributos
[4]. Utilizar sus metodos para asegurar el funcionamiento correcto integro
"""


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def mostrar_datos_personales(self):
        print(f"Me llamo {self.nombre} y tengo {self.edad}")
    

class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad) # Si usamos super, no pasamos self, caso contrario si.
        self.grado = grado
    
    def mostrar_grado(self):
        print(f"Estoy en {self.grado} grado")


estudiante: Estudiante = Estudiante("Fran", 25, 6)


# vars(obj): Devuelve un diccionario con los atributos y valores del objeto

def mostrar_datos(estudiante: Estudiante) -> None:
    for atributo, valor in vars(estudiante).items():
        print(f"{atributo}: {valor}")
    print()
mostrar_datos(estudiante)

estudiante.mostrar_datos_personales()
estudiante.mostrar_grado()