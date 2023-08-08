"""
>>> DECORADORES: Funcion especial que permite modificar el comportamiento
            de otra funcion o metodo sin cambiar su codigo interno. Es como una envoltura
            que se coloca al rededor de una funcion para agregar funcionalidad adicional

    <<< VENTAJAS >>>
    - REUTILIZACION del codigo en una forma elegante y ordenada
    - MEJORA LA LEGIBILIDAD del codigo al eliminar la necesidad de codigo
        repetido en varias funciones
    - EXTENSIBILIDAD porque permiten extender la funcionalidad de una funcion o metodo existente sin
        modificar su codigo original.
    
    PROCESO de la logica del decorador:
    1. Toma una funcion como entrada
    2. Le agrega funcionalidades
    3. Devuelve el resultado de la funcion modificada (la original + modificaciones)

    <<< USOS COMUNES DE LOS DECORADORES >>>
    - Manejo de excepciones: Permite encapsular la logica del manejo de excepciones y 
                            aplicarla a varias funciones de manera consistente y ordenada
    - Validacion de entradas: Permiten agregar logica de validacion antes de que una funcion se ejecute, 
                            asegurando que los valores de entrada cumplan con ciertas condiciones antes de 
                            procesarlos.
                            Es una forma efectiva de garantizar la integridad de los datos y mantener la consistencia
                            en el codigo
    - Medicion del tiempo de ejecucion: Agregan logica para registra el tiempo de inicio y finalizacion de una funcion
    - Control de acceso: Agrega logica pra verificar si un usuario tiene los permisos adecuados para ejecutar una funcion
                        o acceder a ciertos recursos.
                        Ayuda a garantizar la seguridad y privacidad de ciertas partes del codigo, asegurandose que solo
                        usuarios autorizados puedan acceder a ellas
"""


#SINTAXIS Y EJEMPLO
def decorador(funcion): #Decorador: Podemos verlo como un envoltorio de la funcion a modificar
    def funcion_modificada(): #Funcion modificada por el decorador
        print("Antes de llamar a la funcion")
        funcion()
        print("Despues de llamar a la funcion")
    return funcion_modificada #Retorno de la referencia a la funcion_modificada


def saludo():
    print("Hola Usuario")

#APLICAR DECORADOR MANUALMENTE
saludo_modificado = decorador(saludo) #Guardar el resultado de funcion modificada con argumento 'saludo' pero haciendo referencia al objeto
saludo_modificado() #Ejecutamos el decorador


#-----------------------------------------------


#SINTAXIS MAS COMODA O FRECUENTE PARA LLMAR A LOS DECORADORES
@decorador #@funcion-decoradora
def despedida(): #funcion a decorar
    print("Adios usuario, vuelva pronto")

print("\n---------------------\n")
despedida() #Llamar a la funcion a decorar y ejecutarla

