#Ejercicio 1
"""
Funcion que dice si un string tiene algun caracter del alfabeto minuscula, Mayuscula o nuemero
"""
from pytest import importorskip


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
def tiene_h(string):
    import re
    print(bool(re.findall("he*", string)))

def tienehee(string):
    import re
    print(bool(re.findall("he+", string)))

def tiene_he23(string):
    import re
    print(bool(re.search("he{2,3}", string) and not re.search("heeee+", string)))

#Ejercicio 4
"""
Funcion que dice si el string une dos palabras con guion bajo
"""
def unidas_por_guion(string):
    import re
    print(re.findall(r'([a-z]+)_([a-z]+)', string))


#Ejercicio 5
"""
Funcion que dice si un string empieza con x numero especifico
"""
def empieza_con_numero(string, numero):
    import re
    print(bool(re.search("^"+str(numero), string)))


#Ejercicio 6
"""
Funcion que dice si un string de una lista de strings esta en una frase dada
"""
def strings_en_frase(listadestrings,  frase):
    import re
    contador = 0
    for string in listadestrings:
        if re.search(string, frase):
            contador += 1
    print(contador > 0)

#Ejercicio 7
"""
Funcion que encuentra un string que con todos caracteres permitidos y lo imprima
"""
def Stringsoloconcaracterespermitidos(archivo):
    import re
    with open(archivo, "r") as f:
        lineas = f.readlines()
        palabras = lineas.split()
        for palabra in palabras:
            if re.search("^[a-zA-Z0-9_]+$", palabra):
                print(palabra)

#Ejercicio 8
"""
Funcion que devuelve los caracteres numericos de un string
"""
def numeros_en_string(string):
    import re
    print(re.findall("[0-9]", string))

#Ejercicio 9
"""

"""
def devolverstringsentreguiones(string):
    
#Ejercicio 10

#Ejercicio 11
"""
Funcion que devuelve los string que tienen 2 Letras P mayusculas
"""
def dospalabrasempiezenconletrap(listadestrings):
    import re
    for string in listadestrings:
        if re.search("P{2}", string):
            print(string)

#Ejercicio 12
"""
Funcion que devulve un string cambiando sus espacios, guiones bajos y dos puntos por barra vertical
"""
def remplazar_por_barra(string):
    import re
    print(re.sub(r"""[ _:]""", "|", string))

#Ejercicio 14
"""
Funcion que devuelve un string cambiando sus espacios y tabs por ;
"""
def remplazar_por_espacio(string):
    import re
    print(re.sub(r"[    ]",";", string))

#Ejercicio 15
"""
Funcion que se fija si un mail es valido
"""
def validar_mail_correcto(mail):
    import re
    valido = bool(re.match(r'(\S+)@(\w+)\.(\w+)', mail))
    print(valido)
     