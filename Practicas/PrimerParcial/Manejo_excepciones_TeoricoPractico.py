#Desafio 1
#Descargá y ejecutá el script1_manejo_errores.py
#Desafio 2
#Creá una función denominada mitades que tenga como argumento un número e imprima el resultado de la división de ese número por 2
def mitades(numero):
    return numero/2
#Desafio 3
#Cómo mejorarías tu función para que sea capaz de manejar el error de la división por cero? Reescribí la función incorporando una declaración try-except
def mitades(numero):
    try:
        return numero/2
    except TypeError:
        print("El argumento debe ser un número")
    except:
        print("No se puede dividir")

