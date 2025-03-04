#un metodo es una funcion que pertenece a una clase
#un metodo se define dentro de una clase
#un metodo siempre recibe como primer parametro self

class Celular: #Clase
    def __init__(self, marca, modelo, camaraF): #Metodo Constructor
        self.marca = marca #Propiedades
        self.modelo = modelo
        self.camaraF = camaraF

    def llamar(self, numero): #Metodo
        print(f"Llamando al numero {numero}")

    def tomarFoto(self):
        print(f"Tomando una foto con la camara {self.camaraF}")