class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    @property #decorador que permite acceder al atributo nombre como si fuera un atributo de la clase
    def nombre(self):
        return self.__nombre
    
    @nombre.setter #decorador que permite modificar el atributo nombre como si fuera un atributo de la clase
    def nombre(self, newNombre):
        self.__nombre = newNombre

    @nombre.deleter #decorador que permite eliminar el atributo nombre como si fuera un atributo de la clase
    def nombre(self):
        del self.__nombre
    
jobss = Persona("Jobss", 25)
nombre = jobss.nombre #ya no se usa parentesis debido a que se usa el decorador @property
print(nombre) #Jobss

jobss.__nombre = "Roberto" #no se puede modificar el atributo nombre directamente
nombre = jobss.nombre
print(nombre) #Jobss
#En este caso, el atributo nombre es privado, por lo que no podemos modificarlo directamente desde fuera de la clase.

# si quiero modificar el atributo nombre, debo crear un setter
jobss.nombre = "Roberto"
nombre = jobss.nombre
print(nombre) #Roberto
#Para poder modificarlo, creamos un método setNombre que nos permite cambiar el valor del atributo nombre.

# del jobss.nombre
# nombre = jobss.nombre
# print(nombre) #AttributeError: 'Persona' object has no attribute '_Persona__nombre'
#En este caso, el atributo nombre es privado, por lo que no podemos eliminarlo directamente desde fuera de la clase.