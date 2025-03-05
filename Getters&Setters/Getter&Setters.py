# Los Getters y Setters son métodos que nos permiten acceder y modificar los atributos de un objeto de una clase, respectivamente.

class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    def getNombre(self):
        return self._nombre
    
    def setNombre(self, newNombre):
        self._nombre = newNombre
    
jobss = Persona("Jobss", 25)
nombre = jobss.getNombre()
print(nombre) #Jobss
#En este caso, el atributo nombre es privado, por lo que no podemos acceder a él directamente desde fuera de la clase.
#Para poder acceder a él, creamos un método getNombre que nos devuelve el valor del atributo nombre.
#De esta forma, podemos acceder a él de forma segura y controlada.

jobss.setNombre("Roberto")
nombre = jobss.getNombre()
print(nombre) #Roberto
#En este caso, el atributo nombre es privado, por lo que no podemos modificarlo directamente desde fuera de la clase.
#Para poder modificarlo, creamos un método setNombre que nos permite cambiar el valor del atributo nombre.
#De esta forma, podemos modificarlo de forma segura y controlada.