"""
Crea una jerarquía de clases que modele diferentes roles en una institución educativa. Deberás implementar las siguientes clases:
> Persona: Una clase base que tenga atributos comunes como nombre y edad.
> Estudiante: Una clase que tenga atributos como institucion y curso.
> Trabajador: Una clase que tenga atributos como salario y puesto.
> TrabajadorEstudiante: Una clase que herede tanto de Trabajador como de Estudiante. Debe tener todos los atributos de ambas clases base.
Crea instancias de la clase TrabajadorEstudiante y muestra por pantalla los atributos de cada instancia.
"""
# RECOMENDACION: Expresar libertad creativa en el ejercicio. No descuidar el enfoque del mismo y que funcione correctamente


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


class Estudiante:
    def __init__(self, institucion, curso):
        self.institucion = institucion
        self.curso = curso


class Trabajador:
    def __init__(self, salario, puesto):
        self.salario = salario
        self.puesto = puesto


class TrabajadorEstudiante(Persona, Estudiante, Trabajador):
    def __init__(self, nombre, edad, institucion, curso, salario, puesto):
        Persona.__init__(self, nombre, edad)
        Estudiante.__init__(self, institucion, curso)
        Trabajador.__init__(self, salario, puesto)


trabajador_estudiante: TrabajadorEstudiante = TrabajadorEstudiante("Franco", 25, "UBA", "Quimica II A", 500.25, "QA")


print("Nombre ->", trabajador_estudiante.nombre) 
print("Edad ->", trabajador_estudiante.edad) 
print("Institucion ->", trabajador_estudiante.institucion) 
print("Curso ->", trabajador_estudiante.curso)   
print("Salario ->", trabajador_estudiante.salario)
print("Puesto ->", trabajador_estudiante.puesto)