"""
Crea una clase CuentaBancaria con atributos como saldo y
nombre del titular. Agrega métodos para depositar y retirar dinero. 
Realiza algunas operaciones con objetos de esta clase.
"""
#RECOMENDACION: Expresar libertad creativa en el ejercicio. No descuidar el enfoque del mismo y que funcione correctamente


# Importar el modulo os
import os


# Crear de clase
class CuentaBancaria:
    def __init__(self, nombre_titular: str, saldo: float):
        self.saldo = saldo
        self.nombre_titular = nombre_titular
    
    def depositar(self, cantidad: int):
        self.saldo += cantidad
        print(f"Titular: {self.nombre_titular}\n- Se han DEPOSITADO: {cantidad}\n- Su saldo actual es de: {self.saldo}")
    
    def retirar(self, cantidad: int):
        if cantidad < self.saldo:
            self.saldo -= cantidad
            print(f"Titular: {self.nombre_titular}\n- Se han RETIRADO: {cantidad}\n- Su saldo actual es de: {self.saldo}")
        else:
            print("No puede retirar la cantidad ingresada. Supera su saldo disponible")


# Crear instancias de clase
cuenta1: CuentaBancaria = CuentaBancaria("Marcelo Diaz", 100000)
cuenta2: CuentaBancaria = CuentaBancaria("Agustin Gomez", 55250)


# Utilizar metodos
cuenta1.depositar(200)
cuenta2.retirar(500000)
print("\n")


# Aca finaliza el ejercicio, de aca para abajo se realizo un programa mas completo con distintas opciones aplicando programacion estructurada
# -------------------------------------------------------------------------------------------------------------------------------------------


# Procedimiento encargado de mostrar las opciones del programa
def ver_opciones():
    print("""
\t===========================
\t==== CAJERO AUTOMATICO ====
\t===========================

[1] - Alta de cuenta bancaria
[2] - Modificacion de titular en cuenta bancaria
[3] - Baja de cuenta bancaria
[4] - Operaciones cuenta bancaria
[5] - Reporte de base de datos
[6] - Salir
""")
    

# [1] - Alta de cuenta bancaria
def alta_cuenta(cuentas_registradas: list[CuentaBancaria]) -> str:
    titular_cuenta: str = input("Ingresar el nombre del titular de cuenta: ")
    saldo_inicial: float = float(input("Ingresar saldo inicial: "))
    cuenta_nueva: CuentaBancaria = CuentaBancaria(titular_cuenta, saldo_inicial)
    cuentas_registradas.append(cuenta_nueva)
    return f"Se ha dado de alta la cuenta de {titular_cuenta}"


# [2] - Modificacion de titular en cuenta bancaria
def modificar_titular_cuenta(cuentas_registradas: list[CuentaBancaria]) -> str:
    estado_transaccion: str = "No se ha podido completar la transaccion"
    nombre_a_modificar: str = input("Ingrese el nombre completo del titular de la cuenta: ")
    for cuenta in cuentas_registradas:
        if nombre_a_modificar == cuenta.nombre_titular:
            viejo_nombre: str = cuenta.nombre_titular
            nuevo_nombre: str = input("Ingresar nuevo nombre: ")
            cuenta.nombre_titular = nuevo_nombre
            estado_transaccion = f"Se ha modificado el nombre del titular de la cuenta. De {viejo_nombre} a {cuenta.nombre_titular}"
    return estado_transaccion
    

# [3] - Baja de cuenta bancaria
def baja_cuenta(cuentas_registradas: list[CuentaBancaria]) -> str:
    estado_transaccion: str = "No se ha podido completar la transaccion"
    cuenta_a_borrar: str = input("Ingrese el nombre del titular para borrar la cuenta: ")
    for cuenta in cuentas_registradas:
        if cuenta_a_borrar == cuenta.nombre_titular:
            cuentas_registradas.remove(cuenta)
            estado_transaccion = f"Se ha borrado exitosamente la cuenta de {cuenta_a_borrar}"
    return estado_transaccion


# Procedimiento para mostrar opciones de las operaciones bancarias
def mostrar_opciones_operaciones():
    print("""
OPERACIONES BANCARIAS
[1] - Retirar dinero
[2] - Depositar dinero
""")


# [4] - Operaciones cuenta bancaria
def operar_cuentas_bancarias(cuentas_registradas: list[CuentaBancaria]) -> None:
    mostrar_opciones_operaciones()
    titular_cuenta: str = input("Ingrese el nombre de cuenta del titular para realizar operaciones: ")
    OPCIONES: tuple = ("1", "2")
    for cuenta in cuentas_registradas:
        if titular_cuenta == cuenta.nombre_titular:
            opcion: str = input("Ingresar una opcion para continuar:")
            if opcion == OPCIONES[0]:
                cantidad_a_retirar: float = float(input("Ingresar cantidad a retirar: "))
                cuenta.retirar(cantidad_a_retirar)
            elif opcion == OPCIONES[1]:
                cantidad_a_depositar: float = float(input("Ingresar cantidad a depositar: "))
                cuenta.depositar(cantidad_a_depositar)


# Procedimiento encargado de mostrar las bases de datos
def mostrar_reporte(cuentas_registradas: list[CuentaBancaria]) -> None:
    contador: int = 0
    print("=====================================================")
    for cuenta in cuentas_registradas:
        contador += 1
        print(f"[{contador}] - Titular de cuenta: {cuenta.nombre_titular} | Saldo: {cuenta.saldo}")
    print("=====================================================")


# Procedimiento para validar las opciones ingresadas para el menu principal
def validar_opcion_menu(opcion: str):
    OPCIONES_VALIDAS: tuple = ("1", "2", "3", "4", "5", "6")
    while opcion not in OPCIONES_VALIDAS:
        opcion: str = input("Intentar nuevamente... Ingrese una opcion del 1 al 5 para continuar: ")
    return opcion


# Menu principal encargado de ejecutar las funciones y procedimientos de los items 1, 2, 3, 4 y 5
def menu_principal(opcion: str):
    cuentas_registradas: list[CuentaBancaria] = [cuenta1, cuenta2]

    while opcion != "6":
        if opcion == "1":
            print(alta_cuenta(cuentas_registradas))
        elif opcion == "2":
            print(modificar_titular_cuenta(cuentas_registradas))
        elif opcion == "3":
            print(baja_cuenta(cuentas_registradas))
        elif opcion == "4":
            operar_cuentas_bancarias(cuentas_registradas)
        elif opcion == "5":
            mostrar_reporte(cuentas_registradas)
        
        ver_opciones()
        opcion = input("Ingrese una opcion del 1 al 6 para continuar: ")
        opcion = validar_opcion_menu(opcion)
        os.system('cls')

    print("\nGracias por usar el CAJERO AUTOMATICO, hasta luego\n")


# Inicializador del programa
def main():
    ver_opciones()
    opcion: str = input("Ingrese una opcion del 1 al 6 para continuar: ")
    opcion_validada: str = validar_opcion_menu(opcion)
    os.system('cls')
    menu_principal(opcion_validada)
main()