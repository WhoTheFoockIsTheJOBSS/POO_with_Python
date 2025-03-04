#sneik_case: el_nombre_se_divide_con_guiones_bajos
# camelCase: elNombreSeDivideConMayusculas
# PascalCase: ElNombreSeDivideConMayusculasPeroLaPrimeraTambien

#Nota: Las clases se nombran usando PascalCase
#Nota: Las funciones se nombran usando camelCase

#Ejemplo de una clase
class NombreClase(): 
    propiedade1 = "valor1"
    propiedade2 = "valor2"
    propiedade3 = "valor3"

class CelularSamsung(): #Clase
    marca = "Samsung" #Atributo = Propiedades Fijas de la clase 
    modelo = "Galaxy S10"
    camaraF = "12MP"

celular1 = CelularSamsung() #Objeto = instancia de la clase
print(celular1.marca)
print(celular1.modelo)
print(celular1.camaraF)

class Celular: #Clase
    def __init__(self, marca, modelo, camaraF): #Metodo Constructor
        self.marca = marca #Propiedades
        self.modelo = modelo
        self.camaraF = camaraF

iphone13 = Celular("Apple", "Iphone 13", "48MP") #Objeto = instancia de la clase
print(iphone13.marca)
print(iphone13.modelo)
print(iphone13.camaraF)