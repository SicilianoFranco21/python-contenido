"""
> Clases: Plantilla o molde que define como se deben crear los objetos.
            Dichas plantillas o moldes deben tener atributos y comportamientos, 
            que luego adquiriran los objetos que sean instancias de la plantilla o molde

> Objetos: Entidad que agrupa datos (atributos) y comportamientos (metodos) relacionados
            Se dice que es una instancia de una clase

> Atributos: Caracteristicas o propiedades que tienen un objeto. Se acceden
            a los atributos mediante los objetos creados a partir de una clase.
            Representan datos para describir el estado de un objeto
            Ejemplo: Tenemos una clase Persona, tenemos un objeto (instancia de clase persona)
                    llamado Profesor, profesor tiene los atributos de la clase Persona como
                    edad, nombre, apellido, dni
            RECOMENDACION -> Se recomienda usar ATRIBUTOS de INSTANCIA (No estaticos): Son atributos que se definen
                        a la hora de crear un objeto

> Metodos: Acciones que pueden realizar los objetos. Los metodos les permiten a
            los objetos interactuar con otros objetos y con el entorno.
            Los metodos pueden acceder y manipular los atributos del objeto
            Ejemplo: Clase Perro que tiene los metodos "ladrar", "correr", "comer", "dormir". Cada
                    ojbeto de la clase perro podria ejecutar estos metodos

            <<<Metodos especiales >>>
            - CONSTRUCTORES: Se llaman asi porque construyen la clase por cada instancia que se le realiza a la misma                    

            METODOS DE INSTANCIA: Funciones que estan asociadas a una instancia en especifica, esto significa que
                        estos metodos trabajan con los datos particulares de una instancia. 
                        - Los metodos de instancia tiene el primer parametro llamado "self"
                        Ejemplo:
                            class Perro:
                                def __init__(self, nombre):
                                    self.nombre = nombre

                                def ladrar(self):
                                    print(f"{self.nombre} está ladrando")

                            mi_perro = Perro("Max")
                            mi_perro.ladrar()  # Esto imprimirá "Max está ladrando"

            METODOS DE CLASE: Funciones que estan asociadas a la clase en lugar de una instancia especifica. Estos
                        metodos trabajan con datos de la clase en general y no requieren crear una instancia
                        para usarlos. Usamos como primer parametro "cls" (convencion que se refiere a la clase en si)
                        EJEMPLO:
                            class Circulo:
                                pi = 3.14159

                                def __init__(self, radio):
                                    self.radio = radio

                                @classmethod
                                def imprimir_pi(cls):
                                    print(f"El valor de pi es: {cls.pi}")

                            Circulo.imprimir_pi()  # Esto imprimirá "El valor de pi es: 3.14159"          
"""


#Definimos una clase de la siguiente manera (class NombreClase()). Al definir una clase usamos PascalCase
class Celular:
    #Atributos ESTATICOS: POCO COMUN, para todos los objetos van a ser iguales ya que estan predefinidos
    """
    marca = "Samsung"
    modelo = "S23"
    camara = "48MP" 
    """

    # self: Es una referencia a si mismo
    def __init__(self, marca, modelo, camara): #__init__: Es un metodo constructor. Cada vez que instanciamos una clase, este se ejecuta automaticamente. Sirve para definir atributos especificamente por cada instancia
        self.marca = marca #Esto es como decir celular.marca
        self.modelo = modelo #modelo perteneciente a self.modelo, es una propiedad de self. modelo del lado derecho pertenece a init (accedemos a ese parametro) 
        self.camara = camara
    
    #Metodo creado para que la clase Celular realice una accion
    def llamar(self): #Hay que pasarles el parametro self SI o SI a los METODOS DE INSTANCIA
        print(f"Estas haciendo un llamado desde un: {self.modelo}")
    
    def cortar(self):
        print(f"Cortaste la llamada desde un: {self.modelo}")

#Creamos un OBJETO, tipo de dato es object (se almacena en la ram). Le pasamos los parametros que definimos en el __init__
celular1 = Celular("Samsung", "S23", "48PM")
celular2 = Celular("Apple", "Iphone 15 Pro", "96MP")
print(celular1)

#Accedemos al atributo del objeto: objeto.atributo
print(celular1.marca)
print(celular2.marca)

#Utilizamos los metodos
celular1.llamar()
celular2.cortar()