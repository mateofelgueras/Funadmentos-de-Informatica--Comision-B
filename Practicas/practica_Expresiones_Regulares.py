#Ejercicio 1
"""
Funcion que dice si un string tiene algun caracter del alfabeto minuscula, Mayuscula o nuemero
"""
def caracter_permitido(string):
    listaaz = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    lista = list(listaaz)
    palabras = list(string)
    contador = 0
    for c in palabras:
        if c in lista:
            contador += 1
    if contador > 0:
        print("La palabra tiene al menos un caracter permitido")
    else:
        print("La palabra no tiene al menos un caracter permitido")

#Ejercico 2
