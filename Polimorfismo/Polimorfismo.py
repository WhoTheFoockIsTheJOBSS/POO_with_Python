class Gato():
    def sonido(self):
        return "Miau"

class Perro():
    def sonido(self):
        return "Guau"

gato = Gato()
perro = Perro()

# print(gato.sonido())
# print(perro.sonido())   #Polimorfismo: Un objeto puede tener diferentes formas dependiendo de la clase que lo instancie
#En este caso, el objeto gato y perro tienen el mismo metodo sonido pero cada uno tiene un comportamiento diferente

#Polimorfismo con funciones
def hacerSonido(animal):
    print(animal.sonido())

hacerSonido(gato)
hacerSonido(perro)
#En este caso, la funcion hacerSonido recibe un objeto y llama al metodo sonido de dicho objeto

