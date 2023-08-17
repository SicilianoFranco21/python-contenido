"""
Crea una clase Libro con atributos como título, autor y precio.
Utiliza métodos para establecer y obtener el precio y el autor.
Implementa validaciones para asegurarte de que el precio no sea negativo.
"""
# RECOMENDACION: Expresar libertad creativa en el ejercicio. No descuidar el enfoque del mismo y que funcione correctamente


class Libro:
    def __init__(self, titulo, autor, precio):
        self.__titulo = titulo
        self.__autor = autor
        self.__precio = precio

    def validar_precio(self, precio):
        if precio < 0:
            self.__precio = 0
            print("Se ha establecido el valor del precio como 0, corregirlo luego por favor.")
        return precio

    # GETTERS
    def obtener_titulo(self):
        return self.__titulo
    
    def obtener_autor(self):
        return self.__autor

    def obtener_precio(self):
        return self.validar_precio(self.__precio)

    # SETTERS
    def modificar_titulo(self, nuevo_titulo):
        self.__titulo = nuevo_titulo

    def modificar_autor(self, nuevo_autor):
        self.__autor = nuevo_autor

    def modificar_precio(self, nuevo_precio):
        self.__precio = self.validar_precio(nuevo_precio)


libro: Libro = Libro("Witcher", "Tolkkien", 1)


print(libro.obtener_titulo())
print(libro.obtener_autor())
print(libro.obtener_precio())


libro.modificar_titulo("The Witcher")
libro.modificar_autor("Timo Tolki")
libro.modificar_precio(10.5)


print("----------------")
print(libro.obtener_titulo())
print(libro.obtener_autor())
print(libro.obtener_precio())