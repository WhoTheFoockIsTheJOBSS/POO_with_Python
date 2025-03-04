class Persona: #Clase padre
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        return f"Hola, mi nombre es {self.nombre}"

class Empleado(Persona): #La clase Empleado hereda de la clase Persona
    def __init__(self, nombre, edad, nacionalidad, empleo, salario): #Metodo constructor
        super().__init__(nombre, edad, nacionalidad) #Llamamos al metodo constructor de la clase padre
        self.empleo = empleo
        self.salario = salario

Roberto = Empleado("Jobss", 30, "Mexicano", "Programador", 1000)
print(Roberto.hablar())

class Estudiante(Persona):
    def __init__(self, nombre, edad, nacionalidad, universidad, notas):
        super().__init__(nombre, edad, nacionalidad)
        self.universidad = universidad
        self.notas = notas