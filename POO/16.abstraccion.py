"""
ABSTRACCION: Ocultar la complejidad interna de un sistema con el proposito
            de que se pueda usar el mismo conociendo las interacciones basicas, es decir,
            dejando de lado los detalles tecnicos que no son relevantes para un usuario.
            "Concentrarse en el contexto y no en un punto en especifico del mismo"
"""

#EJEMPLO DE ABSTRACCION
class Auto:
    def __init__(self):
        self._estado = "apagado"

    def encender(self):
        self._estado = "encendido"
        print("El auto esta encendido")
    
    #Este es un ejemplo de abstraccion, dado que no necesitamos prenderlo y apagarlo y luego conducir, con conducir lo prenderemos automaticamente
    def conducir(self):
        if self._estado == "apagado":
            self.encender()
        print("Conduciendo el auto")


mi_auto: Auto = Auto()
mi_auto.conducir()
