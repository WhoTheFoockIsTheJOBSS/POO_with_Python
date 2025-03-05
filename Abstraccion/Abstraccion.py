class Auto():
    def __init__(self):
        self._estado = "Apagado"

    def encender(self):
        self._estado = "Encendido"
        print("El auto esta encendido")

    def conducir(self):
        if self._estado == "Apagado":
            self.encender()
            print("El auto esta en movimiento")

miCarro = Auto()
miCarro.conducir() #El auto esta en movimiento