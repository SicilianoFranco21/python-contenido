"""
>>> LSP: Se enfoca en como las sub-clases deben relacionarse con las superclases en un sistema de herencia.
        Establece que una subclase (ya sea actualizada o mejorada con respecto a la clase base) deben poder ser sustituidas
        por su clase base sin alterar el comportamiento del programa. Es decir, la clase-base
        SUSTITUYE a la clase hija sin alterar el programa
        - Todo lo que la clase base haga, tambien lo debe poder hacer la subclase
        - ENFOQUE --> Relacion entre clases y subclases, sustitucion de subclase por clase en los lugares donde la primera existia

    Esto significa:
        Esto significa que, dado que la clase B es una subclase de la clase A, 
        deberíamos poder pasar un objeto de la clase B a cualquier método que espere un objeto de la clase A 
        y el método no debería dar ningún resultado extraño en ese caso.
        Este es el comportamiento esperado, porque cuando usamos la herencia asumimos que la clase secundaria hereda todo 
        lo que tiene la superclase. La clase secundaria extiende el comportamiento pero nunca lo reduce.
        
    >>> EJEMPLO: Construimos una clase Jugador que puede moverse, luego construimos una clase hija JugadorMejorado
                que se mueve mas rapido, segun el LSP, la sub-clase JugadorMejorado deberia SUSTITUIR efectivamente a la clase
                Jugador en todos los lugares donde esta ultima fue implementada

    >>> VENTAJAS
        [1] - EVITA HERENCIA INCORRECTA: Previene situaciones en la que una subclase no puede reemplazar correctamente a su clase base
        [2] - PROMUEVE EL REUSO DE CODIGO: LSP fomenta el reuso del codigo y la creacion de jerarquias de clases mas cohesivas (Esto significa MUY relacionadas entre si para que las partes vinculadas trabajen mejor)
        [3] - FACILITA LA EXTENSIBILIDAD: Disenio ideal para agregar nuevas clases derivadas (subclases) sin afectar el comportamiento existente
        [4] - MEJORA LA CLARIDAD DEL DISENIO: Evita el comportamiento inesperados y las relaciones entre clases y subclases se mantienen claras y coherentes
"""

# CLASE BASE (Super-clase)
class Ave:
    def comer(self):
        return "Estoy comiendo"


# CLASE DERIVADA (Sub-clase)
class AveVoladora(Ave):
    def volar(self):
        return "Estoy volando"


# CLASE DERIVADA (Sub-clase)
class AveNoVoladora(Ave):
    pass


pinguino = AveNoVoladora()
pajaro = AveVoladora()


print("PINGUINO:", pinguino.comer()) # La sub-clase hace todo lo que hace la clase padre
print("PAJARO:", pajaro.comer(), "||", pajaro.volar()) # La sub-clase puede hacer todo lo que la clase base + nuevas funcionalidades