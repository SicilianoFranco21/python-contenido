"""
>>> HERENCIA JERARQUICA: Hay una clasePadre de la cual dependen todas las demas (clasesHijas)
                EJEMPLO: Tenemos la clase Persona que tiene 3 clases hijas (estas dependen de Persona), esas
                        3 clases hijas son Jefe, Estudiante, Empleado. Ya que tienen como  
                        clase base a Persona
"""


def mostrar_datos(objeto: object) -> None:
    tipo_de_dato: str = str(type(objeto))
    
    print(f"""
{objeto.nombre}
{objeto.edad}
{objeto.nacionalidad}""")
    
    if tipo_de_dato == "<class '__main__.Empleado'>":
        print(f"{objeto.trabajo}")
        print(f"{objeto.salario}\n")
    elif tipo_de_dato == "<class '__main__.Estudiante'>":
        print(f"{objeto.notas}")
        print(f"{objeto.universidad}\n")
    elif tipo_de_dato == "<class '__main__.Jefe'>":
        print(f"{objeto.empresa}")
        print(f"{objeto.ganancias}\n")


# Clase Padre
class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print("Hola, estoy hablando un poco")


# Clase Hija
class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario


# Clase Hija
class Estudiante(Persona):
    def __init__(self, nombre, edad, nacionalidad, notas, universidad):
        super().__init__(nombre, edad, nacionalidad)
        self.notas = notas
        self.universidad = universidad


# Clase Hija
class Jefe(Persona):
    def __init__(self, nombre, edad, nacionalidad, empresa, ganancias):
        super().__init__(nombre, edad, nacionalidad)
        self.empresa = empresa
        self.ganancias = ganancias


# Instancia de clase padre Persona
persona_random: Persona = Persona("Chen", 25, "Chino")


# Instancia de clases hijas Empleado, Estudiante, Jefe
# Aqui podemos apreciar la dependencia de las clases hijas con respecto a la clase padre, esto es Herencia Multiple
trabajador: Empleado = Empleado("Fran", 25, "Argentino", "Progrmador", 225000)
alumno: Estudiante = Estudiante("Nico", 24, "Chileno", [7, 8, 9], "UADE")
gerente: Jefe = Jefe("Renzo", 25, "Ingles", "COTO", 0)


mostrar_datos(persona_random)
mostrar_datos(trabajador)
mostrar_datos(alumno)
mostrar_datos(gerente)