#Las clases abtractas son clases que no se pueden instanciar, es decir, no se pueden crear objetos de ellas.
#Estas clases se utilizan para definir una estructura base que será heredada por otras clases, y que estas clases hijass

from abc import ABC, abstractmethod

class Persona(ABC): # esta clase es la plantilla base para las clases hijas
    @abstractmethod
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad

    @abstractmethod
    def hacerActividad(self):
        pass

    def presentarse(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años")


# dalto = Persona("Dalto", 25, "Masculino")
# dalto.presentarse() # arroja error porque no se puede instanciar un objeto de una clase abstracta
#En este caso, la clase Persona es una clase abstracta, por lo que no se puede instanciar un objeto de esta clase.

class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
        
    def hacerActividad(self):
        print(f"Estoy estudiando para ser {self.actividad}")

class Trabajador(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)

    def hacerActividad(self):
        print(f"Actualmente estoy trabajando en un puesto de {self.actividad}")

pedro = Estudiante("Pedro", 25, "Masculino", "Programador")
dalto = Trabajador("Dalto", 28, "Masculino", "Programador")

dalto.presentarse()
dalto.hacerActividad()
pedro.presentarse()
pedro.hacerActividad()