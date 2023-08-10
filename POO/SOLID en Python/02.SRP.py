"""
>>> SRP: Una clase deberia tener una unica razon para cambiar, es decir, una unica responsabilidad
        Cada clase debe hacer solo una tarea/responsabilidad y hacerla bien
        -> Si una clase tiene mas de una funcionalidad, se busca separar en dos clases o mas para que cada clase
            se encargue de una sola cosa
        -> Este principio evita que los desarrolladores creen clases sobrecargadas
        -> IMPORTANTE: cada clase realiza su tarea sin depender de otras clases 
    
    >>> VENTAJAS
            [1] - MANTENIBILIDAD: Es mas facil entender  y cambiar el codigo cuando las responsabilidades estan separadas
                        Si no aplicas SRP, es mas probable que afectes a otras partes del codigo
            [2] - REUTILIZACION: Las clases con responsabilidades unicas son mas faciles de reutilizar en diferentes partes de un proyecto
            [3] - PRUEBAS: Es mas facil realizar pruebas unitarias dado que no hay necesidad de preocuparse por el impacto en otras partes del codigo
            [4] - ESCALABILIDAD: Cuando cada clase tiene su unica responsabilidad, es mas facil agregar nuevas caracteristicas y/o funcionalidades al sistema

    >>> EJEMPLO
        - Escenario: Estamos creando una aplicacion de correo electronico.

        - Aplicacion CON SRP: Dos clases creadas, una para enviar correos y la otra clase para guardar correos en la base de datos
                    Cada clase tiene una unica responsabilidad: Enviar o guardar correos. Si en el futuro necesitas cambiar como se envian
                    los correos, no afectaria como se guardan en la base de datos
        
        - Aplicacion SIN SRP: Una clase creada que envia correos, guarda correos en la base de datos y maneja la auntenticacion de usuarios,
                    esta clase tiene demasiadas responsabilidades. Si se requiere cambiar una parte de esa clase, podria afectar
                    otras partes del codigo y causar problemas inesperados (Hay que estar muchisimo mas atento al SCOPE de los cambios que realicemos)
"""

# UNICA RESPONSABILIDAD: Administrar el combustible
class TanqueDeCombustible:
    def __init__(self):
        self.combustible = 100
    
    def agregar_combustible(self, cantidad):
        self.combustible += cantidad
    
    def obtener_combustible(self):
        return self.combustible

    def usar_combustible(self, cantidad):
        self.combustible -= cantidad


# UNICA RESPONSABILIDAD: Moverse
class Auto:
    def __init__(self, tanque):
        self.posicion = 0
        self.tanque = tanque

    def mover(self, distancia):
        if self.tanque.obtener_combustible() >= distancia/2:
            self.posicion += distancia
            self.tanque.usar_combustible(distancia/2)
            print(f"El auto se movio {distancia} km")
        else:
            print("No hay suficiente combustible")
    
    def obtener_posicion(self):
        return self.posicion


tanque = TanqueDeCombustible()
autito = Auto(tanque)


print("Posicion actual del auto:", autito.obtener_posicion(), "\n")
autito.mover(10)
print("Posicion actual del auto:", autito.obtener_posicion(), "\n")
autito.mover(20)
print("Posicion actual del auto:", autito.obtener_posicion(), "\n")
autito.mover(60)
print("Posicion actual del auto:", autito.obtener_posicion(), "\n")
autito.mover(100)
print("Posicion actual del auto:", autito.obtener_posicion(), "\n")
autito.mover(100)
print("Posicion actual del auto:", autito.obtener_posicion())