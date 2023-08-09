"""
>>> METODOS ESPECIALES (Met. Dunder): Son metodos que permiten realizar funcionalidades especiales
        que con los metodos normales no podriamos lograr. Se los identifica por tener la
        siguiente nomenclatura __metodoEspecial__(*args). Por ejemplo, __init__() es un metodo especial, metodo constructor

    
    >>> Lista de Metodos Especiales
    -> __init__(self, *args): Metodo constructor, ya que permite construir una clase con sus atributos
    -> __str__(): Nos devuelve el una cadena que hayamos definido dentro de dicho metodo y no el ID del objeto. Se llama asi: print(objeto)
    -> __repr__(): Representacion mas detallada y tecnica que devuelve una cadena. Util para depurar, inspeccionar y entender el estado de una instancia de clase
                repr(objeto): La utilizamos para llamar al metodo __repr__
                eval(): Toma una cadena de texto que contiene codigo en algun lenguaje de prog. y lo ejecuta como si fuera parte del programa.
                        Lo podemos pensar como un interprete instantaneo que toma el codigo y lo convierte en
    -> __add__(self, representacion_otro_obj): Suma de instancias de clases. Al hacer la suma se puede realizar con mas de dos objetos e incluso
                                                se pueden utilizar los operadores *, -, /, etc (Siempre y cuando aplique)

"""


class Monstruo:
    def __init__(self, lvl, vida, magia): #Usamos el metodo especial constructor __init__
        self.lvl = lvl
        self.vida = vida
        self.magia = magia
    
    def __str__(self): #Usamos el metodo especial __str__
        return f"Monstruo lvl {self.lvl}\n> HP: {self.vida}\n> MP: {self.magia}"

    def __repr__(self): #Usamos el metodo especial __repr__
        return f"Monstruo({self.lvl}, {self.vida}, {self.magia})"
    
    def __add__(self, otro_monstruo):
        sumar_lvl = self.lvl + otro_monstruo.lvl
        sumar_vida = self.vida + otro_monstruo.vida
        sumar_magia = self.magia + otro_monstruo.magia
        return Monstruo(sumar_lvl, sumar_vida, sumar_magia)


monstruo_lvl20: Monstruo = Monstruo(20, 100, 250)
monstruo_lvl40: Monstruo = Monstruo(40, 200, 500)
print(monstruo_lvl20) #Aca se ve el resultado del metodo __str__
print("--------------")
print(monstruo_lvl40)

print("--------------")
#Para utilizar __add__ debemos sumar dos instancias de clase guardandolas en una variable
monstruo_lvl60: Monstruo = monstruo_lvl20 + monstruo_lvl40
print(monstruo_lvl60)


print("--------------")
#Sumamos 3 terminos de instancia de clase
monstruo_op: Monstruo = monstruo_lvl20 + monstruo_lvl40 + monstruo_lvl60
print(monstruo_op)


print("\n==============\n")
representacion = repr(monstruo_lvl20) #Uso de repr(obj) ya que existe un metodo especial __repr__
print(representacion)


""" 
>>> FORMA NO RECOMENDADA DEBIDO A ...
        ...PROBLEMAS DE SEGURIDAD ya que los usuarios podrian inyectar codigo malicioso
        ...Es mas COMPLEJO, complica la situacion si la clase tiene mas atributos o dependencias adicionales
        ...ALTERNATIVAS MEJORES, es mas claro y seguro crear instancias directametne utilizando el constructor de la clase 

representacion = repr(monstruo)  # Se obtiene la representación oficial como cadena
resultado = eval(representacion)  # Se evalúa la cadena utilizando eval()
print(resultado)  # Se muestra el resultado de eval(), que debería ser un NUEVO OBJETO Monstruo
"""

#codigo_magico = "print('¡Hola, soy una varita mágica de programación!')"
#eval(codigo_magico) 