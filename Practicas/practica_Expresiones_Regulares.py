#Ejercicio 1
"""
Funcion que dice si un string tiene algun caracter del alfabeto minuscula, Mayuscula o nuemero
"""
from pytest import importorskip
from sympy import re


def caracter_permitido(string):
    import re
    print(len(re.findall(r"\w", string)) >0)
#Findall: Lista de todas los coincidentes re.findall(r "lo que queres buscar 
# expresion regular", string)

#Ejercico 2
"""
Funcion que dice si un string tiene todos sus caracteres del alfabeto minuscula, Mayuscula o nuemero
"""
def todos_caracter_permitido(string):
    import re
    print(not len(re.findall(r"\W", string)))

# re findall \W mayuscula hace lista de caracteres no alfanuericos
#len dice cuantos hay de esos caracteres 
# not len si es distinto a 0 es falso.

#Ejercicio 3
"""Funcion que dice si hay h o seguidas de e en un string"""
def tiene_h(string):
    import re
    print(bool(re.findall("he*", string)))
# el asterisco es para que busque todas las combinaciones
# (ab*) busca a, ab y a seguidas de una o mas b

def tienehe(string):
    import re
    print(bool(re.findall("he+", string)))

# (ab+) coincidirá con “a” seguido de cualquier num menos 0 de “b”; no coincidirá solo con “a”.

def tiene_he23(string):
    import re
    print(bool(re.search("he{2,3}", string) and not re.search("heeee+", string)))
# Funcion search comprueba si hay coincidencias que no se limiten al principio

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
# ^ : Inicio de cadena


#Ejercicio 6
"""
Funcion que dice si un string de una lista de strings esta en una frase dada
"""
def strings_en_frase(listadestrings,  frase):
    import re
    for e in listadestrings:
        print(bool(re.search(e, frase)))

#Ejercicio 7
"""
Funcion que encuentra un string que con todos caracteres permitidos y lo imprima
"""
def Stringsoloconcaracterespermitidos(string):
    import re
    import string
    string_sin_espacios = string.replace(" ", "")
    a = bool(re.search(r'[a-z]', string) and re.search(r'[A-Z]', string) and re.search(r"\s", string) and string_sin_espacios.isalnum())
    print(a)
#Isalnum si un string es todo alfanumerico devuelve true


#Ejercicio 8
"""
Funcion que devuelve los caracteres numericos de un string
"""
def numeros_en_string(string):
    import re
    print(re.findall("[0-9]", string))

#Ejercicio 9
"""
Funcion que devuelve las partes de 
"""
def a(string):
    return (re.findall("-.*-", string))
    
#Ejercicio 10
def obtener_substring(substring):
    a = print(re.split("@|&", substring))
    print (a)
#Ejercicio 11
"""
Funcion que devuelve los string que tienen 2 Letras P mayusculas
"""
def dos_con_p(variable):

    for lenguaje in lista_string:
        resultado = re.match("(P\w+)\W(P\w+)", lenguaje)

        if resultado:
            print(resultado.groups())

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
    







