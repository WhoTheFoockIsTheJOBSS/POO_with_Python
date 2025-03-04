class Gato():
    def sonido(self):
        return "Miau"

class Perro():
    def sonido(self):
        return "Guau"

gato = Gato()
perro = Perro()

#Polimorfismo con funciones
def hacerSonido(animal):
    print(animal.sonido())

hacerSonido(gato)
hacerSonido(perro)
#En este caso, la funcion hacerSonido recibe un objeto y llama al metodo sonido de dicho objeto