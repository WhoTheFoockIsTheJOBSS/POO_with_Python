class Estudiante: 
    def __init__(self, Nombre, Edad, Grado):
        self.Nombre = Nombre
        self.Edad = Edad
        self.Grado = Grado

    def estudiar(self):
        print(f'El studiante {self.Nombre} está estudiando')


    
Nombre = input("Ingrese el nombre del estudiante: ")
Edad = input("Ingrese la edad del estudiante: ")
Grado = input("Ingrese el grado del estudiante: ")
Estudiante = Estudiante(Nombre, Edad, Grado)


accion = input("¿Qué desea hacer? estudiar o salir: ")
accion = accion.lower()
while accion != "salir" and accion != "estudiar":
    print("Por favor ingrese una opción válida")
    accion = input("¿Qué desea hacer? estudiar o salir: ")
    accion = accion.lower()

if accion == "estudiar":
    Estudiante.estudiar()
