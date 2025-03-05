from abc import ABC, abstractmethod

class Persona(ABC):
    @abstractmethod
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad

    @abstractmethod
    def trabajar(self):
        pass

    def presentarse(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años")


dalto = Persona("Dalto", 25, "Masculino")
dalto.presentarse() # arroja error porque no se puede instanciar un objeto de una clase abstracta
#En este caso, la clase Persona es una clase abstracta, por lo que no se puede instanciar un objeto de esta clase.

class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)

    def trabajar(self):
        print(f"Estoy estudiando {self.actividad}")

dalto = Estudiante("Dalto", 25, "Masculino", "Programador")