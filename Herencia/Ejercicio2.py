# Herencias - Ejercicio 2
# Ejercicio de herencia y uso de super

# Crear un sistema para escuela. En este sistema, vamos a tener dos clases principales:
# Persona y Estudiante. La clase Persona tenedrá los atributos de nombre, edad y un método
# que imprima el nombre y la edad de la persona. La clase Estudiante Heredará de la clase
# Persona y también tendrá un atributo adicional: grado y un método que  imprima el grado del
# estudiante.

# Deberás utilizar super en el método de inicialización (init) para reutilizar el código de la clase padre
# (Persona). Luego crea una instancia de la clase Estudiante e imprime sus atributos y utiliza sus 
# métodos para asegurarte de que todo funciona correctamente.

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrarPersona(self):
        print(f"Nombre: {self.nombre} Edad: {self.edad}")

class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado

    def gradoEstudiante(self):
        print(f"Grado: {self.grado}")

Estudiante1 = Estudiante("Jobss", 25, "11")

print(Estudiante1.nombre)
print(Estudiante1.edad)
print(Estudiante1.grado)
Estudiante1.mostrarPersona()
Estudiante1.gradoEstudiante()

# Ejercicio de herencia múltiple y MRO
# crea tres clases: "Animal", "Mamifero" y "Ave".
# La clase "Animal" debe tener un método llamado "comer". La clase "Mamifero de tener
# un metodo llamado "amamantar" y la clase "Ave" un método llamado "volar".
# 
# ahora, crea una clase "Murcielago" que Herede de "Mamifero" y "Ave", en ese orden, y por lo tanto
# debe ser capaz de "amamantar", "volar" y "comer".
#
# Finalmente, juega con el orden de la herencia de la clase "Murcielago" y observa cómo cambiar el 
# MRO y el comportamiento de los métodos al user super().

class Animal:
    def comer(self):
        print("El animal come")

class Mamimfer(Animal):
    def amamantar(self):
        print("El animal amamanta")

class Ave(Animal):
    def volar(self):
        print("El animal vuela")

class Murcielago(Mamimfer, Ave):
    pass

animal1 = Murcielago()
print(animal1.comer())
print(animal1.amamantar()) 
print(animal1.volar())