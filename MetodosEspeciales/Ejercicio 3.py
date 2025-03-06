# Crear un juego de fusion
# El juego consiste en crear personajes de un juego y que esos personajes se puedan fusionar
# para formar personajes más poderosos que tengan más poder...

# Para ello deberemos cambiar el comportamiento del operador "+" para que cuando los personajes
# se fusionen, salga un nuevo personaje con habilidades mejoradas.

# una posible formula es: el promedio de las habilidades de ambos, al cuadrado!

class Personaje:
    def __init__(self, nombre, habilidad, poder):
        self.nombre = nombre
        self.habilidad = habilidad
        self.poder = poder

    def __repr__(self):
        return f"{self.nombre} (Habilidad: {self.habilidad}, Poder: {self.poder}) "
    
    def __add__ (self, otro):
        promedio = (self.habilidad + otro.habilidad)/2
        poder = promedio ** 2
        fusion = Personaje(self.nombre + otro.nombre, promedio, poder)
        return Personaje(self.nombre + otro.nombre, promedio, poder)
    

goku = Personaje("Goku", 10, 100)
vegeta = Personaje("Vegeta", 8, 80)

print(goku)
print(vegeta)

fusion = goku + vegeta
print(fusion)