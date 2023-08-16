"""
>>> OCP: Consiste en agregar nuevas caracteristicas sin cambiar el codigo ya existente
        Analogamente podemos decir, que cuando construimos algo, deberia ser como un juguete al que se puede
        agregar mas partes sin tener que romperlo o desarmarlo. Con esto, evitamos romper lo que ya esta hecho
        SIGNIFICADO REAL DE OCP --> "Open for extension, Closed for modify"
        - ENFOQUE --> Extensibilidad del sistema
        
    >>> VENTAJAS
        [1] - EXTENSIBILIDAD: Agregar nuevas funcionalidades al sistema sin modificar el codigo existente
                            Esto facilita la adaptacion del software a los cambios y requisitos futuros
        [2] - MANTENIBILIDAD: Al no tener que modificar el codigo existente para agregar nuevas funcionalidades,
                            se reduce el riesgo de introducir errores o efectos colaterales no deseados. Esto hace
                            que el software sea mas seguro y eficiente
        [3] - ESCALABILIDAD: Capacidad de agregar nuevas funcionalidades sin alterar lo que ya existe, esto es esencial
                            para escalar aplicaciones a medida que crecen en tamanio y complejidad
        [4] - FACILITA PRUEBAS: Al no cambiar el codigo existente para agregar nuevas funcionalidades, las pruebas realizadas
                            en las partes existentes del sistema siguen siendo relevantes ya que se pueden usar los mismos escenarios.
                            Esto simplifica el proceso de QA
"""

# Este es el sistema abierto y generico para agregarle funcionalidades sin modificar lo ya escrito
class Notificador:
    def __init__(self, usuario, mensaje):
        self.usuario = usuario
        self.mensaje = mensaje
    
    def notificar(self):
        raise NotImplementedError


# Funcionalidad agregada (extensibilidad)
class NotificadorEmail(Notificador):
    def Notificar(self):
        print(f"Enviando mensaje via mail a {self.usuario.email}")


# Funcionalidad agregada (extensibilidad)
class NotificadorSMS(Notificador):
    def Notificar(self):
        print(f"Enviando SMS a {self.usuario.sms}")


# Funcionalidad agregada (extensibilidad)
class NotificadorWSP(Notificador):
    def Notificar(self):
        print(f"Enviando WSP a {self.usuario.whatsapp}")


# Funcionalidad agregada (extensibilidad)
class NotificadorTwitter(Notificador):
    def Notificar(self):
        print(f"Enviando WSP a {self.usuario.twitter}")



# ---------------------------------------------------------
# EJEMPLO 2
""" from abc import ABC, abstractmethod

# Definición de clases base (abstracciones)

class GeneradorInforme(ABC):
    @abstractmethod
    def generar(self, datos):
        pass

        
class EstiloInforme(ABC):
    @abstractmethod
    def aplicar(self, contenido):
        pass

        
# Clases concretas (extensiones)

class GeneradorPDF(GeneradorInforme):
    def generar(self, datos):
        contenido = "Contenido del informe en PDF"
        return contenido

        
class GeneradorCSV(GeneradorInforme):
    def generar(self, datos):
        contenido = "Contenido del informe en CSV"
        return contenido

        
class EstiloNormal(EstiloInforme):
    def aplicar(self, contenido):
        return contenido

        
class EstiloResaltado(EstiloInforme):
    def aplicar(self, contenido):
        return f"*** {contenido} ***"

        
# Cliente
class Cliente:
    def __init__(self, generador, estilo):
        self.generador = generador
        self.estilo = estilo
    
    def generar_informe(self, datos):
        contenido = self.generador.generar(datos)
        contenido_con_estilo = self.estilo.aplicar(contenido)
        return contenido_con_estilo

        
# Uso

datos = "Datos importantes"

generador_pdf = GeneradorPDF()
generador_csv = GeneradorCSV()
estilo_normal = EstiloNormal()
estilo_resaltado = EstiloResaltado()

cliente_pdf_normal = Cliente(generador_pdf, estilo_normal)
cliente_csv_resaltado = Cliente(generador_csv, estilo_resaltado)

print(cliente_pdf_normal.generar_informe(datos))
print(cliente_csv_resaltado.generar_informe(datos)) """


# -------------------------------------------------
# EJEMPLO 3
# Definición de la clase base (abstracción)
from abc import ABC, abstractmethod


class FormaGeometrica(ABC):
    @abstractmethod
    def calcular_area(self):
        pass


# Clases concretas (extensiones)

class Rectangulo(FormaGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

class Circulo(FormaGeometrica):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.14159 * self.radio ** 2


# Cliente

def calcular_y_mostrar_area(forma):
    area = forma.calcular_area()
    print(f"El área es: {area}")


# Uso

rectangulo = Rectangulo(5, 3)
circulo = Circulo(2)

calcular_y_mostrar_area(rectangulo)
calcular_y_mostrar_area(circulo)