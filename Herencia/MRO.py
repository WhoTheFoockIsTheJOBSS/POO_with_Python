#MRO: Metodo de Resolucion de Orden
#Metodo donde se resuelve el orden de ejecucion de los metodos de las clases
#En Python se resuelve de izquierda a derecha

class A:
    def hablar(self):
        print("Soy de la clase A")

class B(A):
    def hablar(self):
        print("Soy de la clase B")

class C(A):
    def hablar(self):
        print("Soy de la clase C")

class D(B, C):
    def hablar(self):
        print("Soy de la clase D")

d = D() 
d.hablar()

print(D.mro()) #MRO: D -> B -> C -> A -> object
#con el metodo mro() podemos ver el orden

D.hablar(d) #Soy de la clase D
B.hablar(d) #Soy de la clase B
C.hablar(d) #Soy de la clase C
A.hablar(d) #Soy de la clase A
#puedo ejecutar los metodos de las clases padre de la clase que hereda