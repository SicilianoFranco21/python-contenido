"""
Crea una clase Vehiculo con atributos como marca y modelo. 
Luego, crea subclases Auto y Motocicleta que hereden de Vehiculo. 
Agrega atributos específicos para cada subclase, como la cantidad de 
puertas para el auto y el tipo de motor para la motocicleta.
"""
#RECOMENDACION: Expresar libertad creativa en el ejercicio. No descuidar el enfoque del mismo y que funcione correctamente


#Crear super-clase (Clase padre) Vehiculo
class Vehiculo:
    def __init__(self, marca: str, modelo: str):
        self.marca = marca
        self.modelo = modelo


#Crear sub-clase (clase hija) Automovil
class Automovil(Vehiculo):
    def __init__(self, marca: str, modelo: str, puertas: int):
        super().__init__(marca, modelo)
        self.puertas = puertas


#Crear sub-clase (clase hija) Motocicleta
class Motocicleta(Vehiculo):
    def __init__(self, marca: str, modelo: str, tipo_motor: str):
        super().__init__(marca, modelo)
        self.tipo_motor = tipo_motor


#Instancias de las clases Automovil y Motocicleta
auto: Automovil = Automovil("Ford", "Mondeo", 4)
moto: Motocicleta = Motocicleta("Harley-Davidson", "Street 750", "Gasolina")
auto_pequenio: Automovil = Automovil("Ford", "Fiesta", 2)


#Procedimiento para mostrar los atributos de las instancias de clases
def mostrar_datos(*args) -> None:
    contador: int = 0
    for vehiculo in args:
        tipo: str = str(type(vehiculo))
        contador += 1
        if "Automovil" in tipo:
            print(f"[{contador}] - Automovil --> Marca: {vehiculo.marca} | Modelo: {vehiculo.modelo} | Cantidad de puertas: {vehiculo.puertas}")
        elif "Motocicleta" in tipo:
            print(f"[{contador}] - Motocicleta --> Marca: {vehiculo.marca} | Modelo: {vehiculo.modelo} | Tipo de motor: {vehiculo.tipo_motor}")
        

#Ejecutar mostrar_datos
mostrar_datos(auto, moto, auto_pequenio)