class AtributosProtegidosYPrivados:
    def __init__(self):
        self._atributoProtegido = "Soy un atributo protegido" #Atributo protegido es con un guion bajo
        self.__atributoPrivado = "Soy un atributo privado" #Atributo privado es con dos guiones bajos

class MetodosProtegidosYPrivados:
    def _metodoProtegido(self):
        print("Soy un metodo protegido")

    def __metodoPrivado(self):
        print("Soy un metodo privado")

atributos = AtributosProtegidosYPrivados()
print(atributos._atributoProtegido) #Soy un atributo protegido
print(atributos.__atributoPrivado) #AttributeError: 'AtributosProtegidosYPrivados' object has no attribute '__atributoPrivado'

metodoProtegido = MetodosProtegidosYPrivados()
metodoProtegido._metodoProtegido() #Soy un metodo protegido
metodoProtegido.__metodoPrivado() #AttributeError: 'MetodosProtegidosYPrivados' object has no attribute '__metodoPrivado'
#En Python no existe el encapsulamiento como tal, pero se puede simular con atributos y metodos protegidos y privados
