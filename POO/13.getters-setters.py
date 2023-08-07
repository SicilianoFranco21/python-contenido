"""
>>> GETTERS Y SETTERS: Ambos son metodos especiales utilizados
            para acceder y modificar atributos de una clase de forma controlada.
            -> Permiten mantener la encapsulacion y abstraccion

            
    CASOS DE USO:
            [1] - ENCAPSULACION: La modificacion y acceso de los atributos estan controlados por los metodos de la clase
            [2] - VALIDACION DE DATOS: Los setters permiten validar los datos antes de asignarlos a los atributos
            [3] - ABSTRACCION: Pueden ocultar los detalles internos de implementacion de una clase y proporcionar una interfaz mas
                        sencilla y amigable para interactuar con la clase
            [4] - CONTROL DE ACCESO: Controlan el acceso a ciertos atributos de una clase
-----------------------------------------------

>>> GETTERS: Se utiliza para OBTENER el valor de un atributo privado de una clase
            desde fuera de la clase

            
    <<< EJEMPLO >>>
    class Persona:
        def __init__(self, nombre):
            self.__nombre = nombre

        def get_nombre(self):
            return self.__nombre

-----------------------------------------------

>>> SETTERS: Se utiliza para MODIFICAR el valor de un atributo privado de una clase
            desde fuera de la clase


    <<< EJEMPLO>>> 
    class Persona:
        def __init__(self, nombre):
            self.__nombre = nombre

        def set_nombre(self, nuevo_nombre):
            self.__nombre = nuevo_nombre 
"""
