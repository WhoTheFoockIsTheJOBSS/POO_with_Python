#Polimorfismo por herencia
#Este tipo de Polimorfismo no es aplicable en Python, ya que Python no soporta la sobrecarga de metodos
#Para simular el polimorfismo por herencia, se puede hacer uso de la palabra reservada pass

class Animal:
    def sonido(self):
        pass

class Gato(Animal):
    def sonido(self):
        return "Miau"

class Perro(Animal):
    def sonido(self):
        return "Guau"

gato = Gato()
perro = Perro()