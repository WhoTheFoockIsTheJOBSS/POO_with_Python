#codiog de ejenplo de decoradores
#Un decorador es una funcion que recibe otra funcion como parametro y retorna una nueva funcion
#La funcion decorada se ejecuta antes de la funcion original
#Para decorar una funcion, se debe colocar el decorador antes de la definicion de la funcion
#En este caso, la funcion decorador recibe la funcion saludo como parametro y retorna una nueva funcion
#La nueva funcion imprime un mensaje antes de llamar a la funcion original
#Finalmente, se llama a la funcion decorada

def decorador(funcion):
    def funcionModificada():
        print("Antes de llamar a la funcion")
        funcion()
    return funcionModificada

# def saludo():
#     print("Hola")

# saludoModificado = decorador(saludo)
# saludoModificado()

#codigo optimizado
#la diferencia es que se coloca el decorador antes de la definicion de la funcion
#En este caso, la funcion saludo es decorada por la funcion decorador

@decorador
def saludo():
    print("Hola")

saludo()