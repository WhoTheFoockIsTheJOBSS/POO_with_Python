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

class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad

    def mostrarHabilidad(self):
        print(f"Mi habilidad es {self.habilidad}")

class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.salario = salario
        self.empresa = empresa

    def mostrarHabilidad(self):
        return "No tengo gg"
    
    def presentarse(self):
        #retunr self.mostrarHabilidad() #mostrarHabilidad de la clase hija(EmpleadoArtista)
        #return super().mostrarHabilidad() #mostrarHabilidad de la clase padre(Artista)
        return f'Hola, soy {self.nombre}, mi habilidad es {self.habilidad} y trabajo en {self.empresa}'
    
jobss = EmpleadoArtista("Jobss", "25", "Mexicano", "Programador", 20000, "Capgemini")
print(jobss.presentarse())

#saber si un objeto es instancia de una clase
instancia =  isinstance(jobss, EmpleadoArtista) #True

#saber si una clase es subclase de otra
herencia = issubclass(EmpleadoArtista, Persona) #True  