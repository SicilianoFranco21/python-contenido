"""  
>>> MRO (Method Resolution Order): Asegura el correcto funcionamiento de la herencia multiple.
            El MRO determina el orden en el que Python buscara los atributos y metodos de las clases
            padres

<<< EJEMPLO >>>
class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

> Logica del orden -> Como la primera clase padre es B, busca en B, luego en C. Y si no esta dentro de los parentesis busca en A        
> ORDEN DE BUSQUEDA - > (D, B, C, A)
        - Como observamos, primero busca de las clases padres directas, luego busca en la clase padres mas arriba (jerarquicamente)
        - Primero buscan en D, luego va a B, luego a C, y luego a A (clase "abuela" de clase D)
"""

#-----------------------------------------------------------------------

#EJEMPLO MAS COMPLEJO
"""
>>> ORDEN DE BUSQUEDA -> D, B, A, C, F

>>> LOGICA del ORDEN en caso de heredar de distintos lugares:
1. Si D no lo tiene busca en B (perteneciente a la rama A tambien)
2. Si B no lo tiene busca en A (raiz de la rama A)
3. Si A no lo tiene busca en C (perteneciente a la rama F)
4. Si C no lo tiene busca en F (raiz de la rama F)

>>> RESUMEN DE LOGICA: Primero busca dentro de la clase propia, luego busca dentro de la primera clase heredada
teniendo en cuenta que es de la rama "A", luego si la clase heredada de la rama A no lo tiene
va a buscar en la propia clase A, y si a no lo tiene, luego va por la rama F
"""
class A:
    #def hablar(self):
    #    print("Hola desde A")
    pass

class F:
    def hablar(self):
        print("Hola desde F")

class B(A):
    #def hablar(self):
        #print("Hola desde B")
    pass

class C(F):
    #def hablar(self):
    #    print("Hola desde C")
    pass

class D(B, C):
    #def hablar(self):
        #print("Hola desde D")
    pass

d = D()
d.hablar()

# VER EL MRO con el metodo ---> .mro()
print(D.mro())


"""
>>> La forma de ejecutar un metodo de mas arriba (clase mas arriba) con el objeto de
abajo, para que se ejecute con el mismo, es la que se ve a continuacion

>>> Para ejecutar un metodo de un objeto que es instancia de una clase "X" desde
una clase "Y" hacemos lo siguiente:
objeto = X()
Y.metodo(objeto)
"""

de = D()
F.hablar(d)