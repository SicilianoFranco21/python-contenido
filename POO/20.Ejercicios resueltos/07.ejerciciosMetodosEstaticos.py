"""
Crea una clase Calculadora con métodos estáticos para sumar, 
restar, multiplicar y dividir dos números (RETO: Que al menos un metodo estatico reciba n parametros). Luego, utiliza estos
métodos sin necesidad de crear instancias de la clase.
"""
# RECOMENDACION: Expresar libertad creativa en el ejercicio. No descuidar el enfoque del mismo y que funcione correctamente


# Crear clase Calculadora con sus met. estat. (@staticmethod se utiliza por buenas practicas, aunque es innecesario para la ejecucion correcta del programa)
class Calculadora:
    @staticmethod
    def sumar(*args: float) -> float:
        suma_total: float = 0
        for n in args:
            suma_total += n
        return float(suma_total)
    
    @staticmethod
    def restar(x: float, y: float) -> float:
        return float(x - y)
    
    @staticmethod
    def dividir(x: float, y: float) -> float:
        return float(x/y)
    
    @staticmethod
    def multiplicar(*args: float) -> float:
        multiplicacion_total: float = 1
        for n in args:
            multiplicacion_total *= n
        return float(multiplicacion_total)


# Llamar al metodo de clase (Observar que no es necesario crear instancias para utilizar el metodo estatico de clase)
print(f"Suma: {Calculadora.sumar(2, 3, 5)}")
print(f"Resta: {Calculadora.restar(4, 3)}")
print(f"Division: {Calculadora.dividir(15, 3)}")
print(f"Multiplicacion: {Calculadora.multiplicar(2, 3, 5)}")
        
                
            