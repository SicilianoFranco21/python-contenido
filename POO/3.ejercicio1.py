""" 
1. Crear clase estudiante
2. Crear atributos nombre, edad y grado
3. Crear metodo estudiar()
4. Crear un objeto Estudiante y usar el metodo estudiar()
"""
import os


class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    
    def estudiar(self):
        print(f"El estudiante {self.nombre} esta estudiando")


def crear_estudiante() -> Estudiante:
    nombre = input("Digame su nombre: ")
    edad = input("Digame su edad: ")
    grado = input("Por ultimo, su grado: ")
    estudiante = Estudiante(nombre, edad, grado)
    print()
    return estudiante


def elegir_estudiante(estudiantes) -> Estudiante:
    nombre_estudiante: str = input("Ingresar nombre de estudiante: ")
    estudiante_encontrado: Estudiante = ""
    for estudiante in estudiantes:
        if nombre_estudiante == estudiante.nombre:
            estudiante_encontrado = estudiante
    return estudiante_encontrado


def dar_ordenes(estudiante_encontrado) -> None:
    if estudiante_encontrado == "":
        print("No se encuentra el estudiante para darle ordenes")
    else:
        estudiante_encontrado.estudiar()


def mostrar_estudiante(estudiantes) -> None:
    iterador: int = 0
    for estudiante in estudiantes:
        print(f"> Detalles del estudiante {iterador + 1}")
        print(f"Nombre: {estudiante.nombre}")
        print(f"Edad: {estudiante.edad}")
        print(f"Grado: {estudiante.grado}\n")
        iterador += 1


def validar_cantidad_estudiantes(estudiantes) -> None:
    cantidad_estudiantes: int = len(estudiantes)
    if cantidad_estudiantes == 0:
        print("No hay estudiantes registrados!\n")
    else:
        mostrar_estudiante(estudiantes)


def mostrar_opciones() -> None:
    print("""
Opciones
1. Ingresar estudiante
2. Dar ordenes a un estudiante
3. Ver estudiantes registrados
4. Salir
""")


def menu_principal(opcion) -> None:
    estudiantes: list = []
    OPCIONES_VALIDAS: tuple = ("1", "2", "3", "4")
    while opcion != "4":
        if opcion == OPCIONES_VALIDAS[0]:
            estudiante: Estudiante = crear_estudiante()
            estudiantes.append(estudiante)
        elif opcion == OPCIONES_VALIDAS[1]:
            encontrar_estudiante: Estudiante = elegir_estudiante(estudiantes)
            dar_ordenes(encontrar_estudiante)
        elif opcion == OPCIONES_VALIDAS[2]:
            validar_cantidad_estudiantes(estudiantes)
        elif opcion not in OPCIONES_VALIDAS:
            print("Ingrese una opcion valida por favor\n")
        
        mostrar_opciones()
        opcion: str = input("Ingresar una opcion: ")
        os.system('cls')
    print("HASTA LUEGO")


def main() -> None:
    mostrar_opciones()
    opcion: str = input("Ingresar una opcion: ")
    os.system('cls')
    menu_principal(opcion)
main()
