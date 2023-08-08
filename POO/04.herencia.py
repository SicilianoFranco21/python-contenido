"""
>>> HERENCIA: Le permite a la clase hija acceder a todos los metodos y
        tener las propiedades de la clase padre
        EJEMPLO 1: Tengo una clase Persona (clase padre) y clase Estudiante (clase hija)
                La clase estudiante heredara todo de la clase padre y ademas, realizar cosas nuevas

        EJEMPLO 2: Tenes una clase galletita, con propiedades harina, huevo y azucar. Para
                Evitar crear constantemente la clase galletita y agregarle cosas, podemos resumir el 
                proceso haciendo lo siguiente, utilizar la clase galletita como molde y crear dos clases
                hijas que hereden las propiedades de la clase galletita, a partir de esta
                se crearan la clase Galletita_avena_y_pasas y Galletita_de_chocolate, estas dos simplemente 
                se les agregara los ingredientes necesarios, ya que la base la tienen gracias a la herencia por parte
                de la clase Galletita


<<< Sintaxis >>>

class ClaseHija(ClasePadre)
    def __init__(self, propiedadHeredada1, propiedadHeredada2, nuevaPropiedad1)
        super().__init__(propiedadHeredada1, propiedadHeredada2)
        self.nuevaPropiedad1 = nuevaPropiedad1

EXPLICACIONES
super(): Llama a metodos y accede a propiedades de una clase padre desde una clase hija. Se obtiene referencia a la clase padre
super().__init__(propiedadesHeredadas)
"""


class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print("Hola, estoy hablando un poco")


class Empleado(Persona):
    #Esto es como un constructor dentro de otro constructor
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario

    def hablar(self):
        print("No puedo hablar en el trabajo")

     
franco = Empleado("franco", 25, "argentino", "programador", 225000)
franco.hablar()