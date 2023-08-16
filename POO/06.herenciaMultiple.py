"""
>>> HERENCIA MULTIPLE: Misma logica que la Herencia per se, con la unica diferencia
                de que una clase hija, puede heredar de 2 o mas clases padres

<<< Sintaxis >>>
- Igual que en la de herencia. Con la diferencia de que no usamos super()__init__()
- USAMOS la clase de la que hereda seguida de un punto y luego init y sus propiedades correspondientes
EJEMPLO:
    class EmpleadoArtista(Persona, Artista):
        def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
            Persona.__init__(nombre, edad, nacionalidad)
            Artista.__init__(habilidad)
"""


# Clase Padre
class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print("Hola, estoy hablando un poco")


# Clase Hija
class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad
    
    def mostrar_habilidad(self):
        return f"Mi habilidad es: {self.habilidad}"


# Clase Hija
class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, empresa, salario):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.empresa = empresa
        self.salario = salario

    def presentarse(self):
        print(f"Hola, soy {self.nombre}. {self.mostrar_habilidad()}. Trabajo en {self.empresa}")
        # >>> return f"Hola soy Franco. {super().mostrar_habilidad()}" #De esta manera accedemos al metodo padre, con super()
        # >>> return f"Hola soy Franco. {self.mostrar_habilidad()}" #Accedemos al metodo de la propia clase, ya que self es una referencia asi mismo

roberto: EmpleadoArtista = EmpleadoArtista("Roberto", 43, "Argentino", "Cantar", "Google", 100000)
roberto.presentarse()

# issubclass(clase1, clase2): Valida la clase 1 hereda de la clase 2. True si es verdadero, caso contrario, false
herencia: bool = issubclass(EmpleadoArtista, Artista)
print("Instancia herencia:", herencia)


# isinstance(objeto, clase): Valida si el objeto es una instancia de la clase. Ture si es verdadero, caso contrario, false
instancia: bool = isinstance(roberto, EmpleadoArtista)
print("Instancia 'instancia':", instancia)