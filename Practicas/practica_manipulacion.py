from os import pread
from urllib.parse import _ParseResultBase
path = "C:\Users\mateo\Desktop\UCEMA\manipulacion_archivos.txt"

#Ejercicio 1
def lineadearchivo(archivo, letra):
    """
    Funcion que lee un archivo y dice cuantas lineas empiezan con n letra
    """
    with open(archivo, "r") as f:
        contador = 0
        for linea in f:
            if linea.startswith(letra):
                contador += 1
    print(contador)
"""
Startswith se fija si el valor ingresado coincide con el principio
del string
"""

#Ejercicio 2
def imprimirnlineas(archivo, n):
    """
    Funcion que lee un archivo y imprime las n primeras lineas
    """
    with open(archivo, "r") as f:
        for i in range(n):
            print(f.readline())
"""
RANGE genera un bucle que imprime las lineas con READLINE()
"""
#Ejercicio 3
def nulineas(archivo, n):
    """
    Leer archivo y imprimir las n ultimas lineas, previamente guardadas
    """
    with open(archivo, "r") as f:
         print(f.readlines[-n:])

"""
.READLINES() devuelve una lista con todas las lineas del archivo, 
cada uno como elemento. Despues se llama al final de la lista con [-n:].
"""
#Ejercicio 4
def cuantaspalabrasarchivo(archivo):
    """
    Leer archivo y cuantas palabras tiene
    """
    with open(archivo, "r") as f:
        linea = f.read()
        palabras = linea.split()
        return len(palabras)
"""
.READ() lee el archivo entero, con el split separa las palabras 
por espacios en una lista, y se cuentan los elementos de la lista
con len.
"""
#Ejercicio 5
"""
Lee archivo y cambia n letra por esa letra y un salto de linea
"""
def remplazar_letra(archivo, letra):
    import re
    with open(archivo, "r") as f:
        linea = f.read()
        lineas = linea.replace(letra, letra + "\n")
        with open("archivo_nuevo", "w") as f2:
            f2.write(lineas)
"""
Lee al archivo con read remplaza toda las letras por 
un salto de linea. Abre un archivo nuevo para escribir
y escribe el contenido con el salto de linea con el .WRITE().
"""

#Ejercicio 6
"""
Lee archivo y sacar los saltos de linea
"""
def sin_salto_de_linea(archivo):
    with open(archivo, "r") as f:
        linea = f.read()
        lineas = linea.replace("\n", "")
        with open("archivo_nuevo", "w") as f2:
            f2.write(lineas)

#Ejercicio 7
def maslarga(archivo):
    """
    Leer archivo y arrojar palabra mas larga
    """
    with open(archivo, 'r') as f:
        palabras = f.read().split()
        maslarga = max(palabras, key=len)
    return print("La palabra mas larga es:", maslarga, "con", len(maslarga), "caracteres")

#Ejercicio 8
def Joinfiles(file1, file2, file3):
    """
    Junta dos archivos en uno nuevo
    """
    with open(file1, "r") as f1, open(file2, "r") as f2, open(file3, "a") as f3:
        f3.write(f1.read() + f2.read())
Joinfiles("Docuemento 1", "Documento 2", "Documento 3")
"""
Se abren todos los archivos, los primeros como r para leer
y el segundo como a para agregar, despues se escribe en el 3
el .READ de los dos.
"""
#Ejercicio 9
"""
Funcion que lee un archivo y arroja la frecuencia de n palabra
"""
def frecuencia_palabra(archivo, palabra):
    with open(archivo) as f:
        linea = f.read()
        palabras = linea.split()
        contador = 0
        for i in range(len(palabras)):
            if palabras[i] == palabra:
                contador += 1
        return contador/len(palabras)

#Ejercicio 10
def  agregararchivos(path_carpeta):
    """
    Funcion que añade a un archivo dado todos los archivos de texto (.txt) que hayan en una determinada carpeta.
    """
    import os
    lista = os.listdir(path_carpeta)
    for i in lista:
        if i.endswith(".txt"):
            with open("documento", "a") as f:
                with open(i, "r") as f2:
                    f.write(f2)
   
"""
os.listdir() devuelve una lista con todos los 
archivos de una carpeta. Despues se fija para cada elemento de 
la lista, si termina en .txt, se agrega al archivp nuevo.
"""



