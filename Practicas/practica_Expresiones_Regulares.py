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
"""
Funcion que dice si un string tiene todos sus caracteres del alfabeto minuscula, Mayuscula o nuemero
"""
def todos_caracter_permitido(string):
    listaaz = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    lista = list(listaaz)
    palabras = list(string)
    contador = 0
    for c in palabras:
        if c in lista:
            contador += 1
    if contador == len(string):
        print("La palabra tiene todos sus caracteres permitidos")
    else:
        print("La palabra no tiene todos sus caracteres permitidos")

#Ejercicio 3
def hseguguidadee(string):
    import re
    re.search("h", string)

#Ejercicio 4
"""
Funcion que dice si el string une dos palabras con guin bajo
"""
def palabraconguionbajo(string):
    import re
    print(bool(re.search("_", string)))

#Ejercicio 5
"""
Funcion que dice si un string empieza con x numero especifico
"""
def empieza_con_numero(string, numero):
    import re
    print(bool(re.search("^"+str(numero), string)))


#Ejercicio 6
