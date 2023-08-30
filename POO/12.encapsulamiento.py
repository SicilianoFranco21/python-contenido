"""
>>> ENCAPSULAMIENTO: Forma de proteger los datos de una clase para
            que solo puedan ser accedidos y modificados de manera controlada.
            Es como poner tus datos importantes en un cofre (la clase) y proporcionarle
            una llave especial (metodos) para interactuar con
            esos datos. 
            Tres tipos de encapsulamiento, publico, protegido y privado
    
    -------------------------------------------------------------------------------------------
    
    >>> SINTAXIS:
        -> Atributos "publicos": Son accesibles desde cualquier lugar, tanto desde dentro como desde fuera de la clase.
            Se accede a ellos utilizando la siguiente notacion: objeto.atributo
        
        -> Atributos "protegidos": Son accessibles desde dentro de la clase y tambien desde las clases derivadas (hijas). 
            Su acceso se hace generalmente utilizando la notacion del punto, igual que los publicos
            En python, las variables llevan un guion bajo al principio, para indicar que no se acceda al dato
        a menos que se sepa a detalle lo que sucede. Se puede acceder a ellas llamandolas
        Ejemplo:
            def __init__(self, atributo1, atributo2, atributo3):
                self._atributo1 = atributo1

        
        -> Atributos "privados": Atributos solo accesibles desde dentro de la clase en la que se definen, se utilizan getters
            y setters para acceder a ellos. En python, se indican las variables con un doble guion bajo
            al principio. La unica manera de acceder a ellas es mediante metodos enfocados a obtener y/o editar propiedades
            def __init__(self, atributo1, atributo2, atributo3):
                self.__atributo1 = atributo1
    
    -------------------------------------------------------------------------------------------
    
    >>> VENTAJAS: 
        1. Seguridad: Evita que los datos importantes sean modificados, lo que ayuda a
                prevenir errores y fallos en el programa
        2. Modularidad: Permite cambiar la implementación interna de una clase sin afectar el resto
                del programa, siempre que los metodos publicos sigan funcionando de la
                misma manera
        3. Ocultamiento de información: Oculta los detalles internos de una clase, lo que facilita su uso
            para otros desarrolladores sin necesidad de conocer como funciona internamente

    -------------------------------------------------------------------------------------------

    >>> EJEMPLO:
class TarjetaCredito:
    def __init__(self, numero, vencimiento, codigo_seguridad):
        self.__numero = numero
        self.__vencimiento = vencimiento
        self.__codigo_seguridad = codigo_seguridad

    def obtener_numero(self):
        return self.__numero

    def obtener_vencimiento(self):
        return self.__vencimiento

    # No proporcionamos un método para obtener el código de seguridad, ya que es información sensible

# Uso de la clase TarjetaCredito
tarjeta = TarjetaCredito("1234-5678-9012-3456", "12/25", "789")

# Intentar acceder directamente al código de seguridad (esto dará un error)
# print(tarjeta.__codigo_seguridad)

# Obtener el número y fecha de vencimiento a través de los métodos públicos
print(tarjeta.obtener_numero())       # Salida: 1234-5678-9012-3456
print(tarjeta.obtener_vencimiento())  # Salida: 12/25
"""

# Los ejemplos estaran enfocados en ser casos que no den error


# Ejemplo con atributos privados
class Persona:
    def __init__(self, nombre, dni):
        self.__nombre = nombre
        self.__dni = dni
    
    def obtener_nombre(self):
        return self.__nombre
    
    def obtener_dni(self):
        return self.__dni
    
    def obtener_datos(self):
        return f"Nombre: {self.__nombre} || DNI: {self.__dni}"
    

class Credencial(Persona):
    def __init__(self, nombre, dni, contrasenia):
        super().__init__(nombre, dni)
        self.__contrasenia = contrasenia
    
    def obtener_contrasenia(self):
        return self.__contrasenia

# ...

persona = Persona("Franco", 41123123)
tarjeta = Credencial("Franco", 41123123, "contraseniafalsa123")

print(tarjeta.obtener_contrasenia())
print(tarjeta.obtener_nombre())
print(tarjeta.obtener_dni())
print(tarjeta.obtener_datos())


print("\n")


# Ejemplo con atributos publicos
class EncapsulamientoPublico:
    def __init__(self):
        self.atributo_publico = "Este es un atributo público"
        
    def metodo_publico(self):
        return "Este es un método público"

objeto = EncapsulamientoPublico()

print(objeto.atributo_publico)
print(objeto.metodo_publico())


print("\n")


# Ejemplo con atributos protegidos
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self._edad = edad  # Atributo protegido

class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado
        self._calificaciones = {}  # Atributo protegido
    
    def agregar_calificacion(self, materia, calificacion):
        self._calificaciones[materia] = calificacion
    
    def obtener_calificaciones(self):
        return self._calificaciones

# Crear un estudiante y agregar calificaciones
estudiante = Estudiante("Ana", 17, "11º grado")
estudiante.agregar_calificacion("Matemáticas", 95)
estudiante.agregar_calificacion("Historia", 85)
estudiante.agregar_calificacion("Inglés", 90)

# Obtener calificaciones
calificaciones = estudiante.obtener_calificaciones()
print(calificaciones)