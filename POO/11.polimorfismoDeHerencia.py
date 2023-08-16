"""
### NO NECESITAMOS USAR EL POLIMORFISMO DE HERENCIA EN PYTHON ###
POR QUE?
-> Por el "Duck Typing" ... "Si camina como un pato y hace cuac cuac, entonces es un pato. En otras palabras, si un 
    objeto tiene los metodos y atributos necesarios para realizar una operacion especifica, Python no se 
    preocupa por su tipo o clase, sino que permite que el objeto realice la operacion
-> Python permite que las funciones y los metodos acepten parametros de diferentes tipos y manejen cada tipo de
    forma adecuada.
-> A diferencia de Java o C++, Python no necesita declarar interfaces explicitas para lograr el polimorfismo. Cualquier
    objeto que implemente los metodos esperados, se puede utilizar de manera polimorfica
    

>>> POLIMORFISMO de HERENCIA (Tambien llamado Polimorfismo de Subtipo/Subclase)
    -> Este concepto significa que las clases hijas pueden comportarse de
        distintas maneras, pero todas ellas se basan en la misma clase base. Cada
        clase hija tiene sus propias caracteristicas y metodos unicos, pero
        tambien puede compartir algunos con la clase base
    -> Cualquier objeto que comparta una interfaz comun (metodos y atributos) puede ser utilizado polimorficamente en Python
    -> PARA QUE SE USA? 
        Nos permite escribir codigo mas generico y flexible
        EJEMPLO: Si tenemos una lista de animales, podemos recorrerla y 
                llamar al metodo hacer_sonido() para cada animal y cada uno,
                sabra responder de forma diferente
    -> RESUMEN: el polimorfismo de herencia nos permite crear clases que pueden comportarse de manera diferente, 
                pero comparten características comunes gracias a la herencia
"""


class Animal:
    def hacer_sonido(self):
        print("Ruido desconocido")

class Perro(Animal):
    def hacer_sonido(self):
        super().hacer_sonido() # Esto no es necesario
        print("Guau guau")

class Gato(Animal):
    def hacer_sonido(self):
        print("Miau miau")

class Pajaro(Animal):
    def hacer_sonido(self):
        print("Pío pío")

# Crear una lista con instancias de las clases
animales: list = [Animal(), Perro(), Gato(), Pajaro()]

# Llamar al método hacer_sonido() en cada instancia usando un bucle for
for animal in animales:
    animal.hacer_sonido()


perro: Perro = Perro()
perro.hacer_sonido()
