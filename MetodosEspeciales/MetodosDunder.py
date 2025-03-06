class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__ (self):
        return f'Persona(nombre={self.nombre}, edad={self.edad})'
    
    def __repr__(self):
        return f'Persona("{self.nombre}", {self.edad})'
    
    def __add__(self, otro):
        nuevoValor = self.edad + otro.edad
        return Persona(self.nombre + otro.nombre, nuevoValor)

dalto = Persona("Dalto", 25)
pedro = Persona("Pedro", 30)

nuevaPersona = dalto + pedro
print(nuevaPersona)