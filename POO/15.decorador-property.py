"""
>>> Decorador @property: Permite controlar como se accede a un
                atributo de una clase.
                - Es una forma de hacer que ciertos metodos se comporten
                como si fueran atributos, proporcionado un nivel adicional de
                encapsulacion y seguridad en las clases.
                - Solo se pueden modificar con un setter especial

>>> Decorador @nombre-atributo.setter: Permite modificar un atributo
                                        restringido por el nivel extra
                                        de encapsulacion gracias a
                                        @property

>>> UTILIDADES:
    - controlar el acceso y modificacion de los atributos de una clase en Python
    - Dar un nivel adicional de encapsulacion y seguridad al trabajar con atributos
"""


class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
    
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
    
    @nombre.deleter # decorador para eliminar propiedades, sin este no se puede
    def nombre(self):
        del self.__nombre # del: Operador que nos elimina valores


persona: Persona = Persona("Mike", 24)
nombre = persona.nombre # Si se intenta modificar el atributo tira un error, dado que es un getter, no setter
print(nombre) # No se puede modificar de ninguna manera, ni con: persona.__nombre = "nuevo nombre", persona.nombre = "nuevo nombre"
# Notemos que ni con el acceso a la variable original (privada) ni con la del getter podemos modificar el nombre

persona.nombre = "Franco"
actualizar_nombre = persona.nombre
print(actualizar_nombre)


""" 
>>> Ejemplo con el decorador .deleter
del persona.nombre
ver_nombre = persona.nombre
print(ver_nombre) """


