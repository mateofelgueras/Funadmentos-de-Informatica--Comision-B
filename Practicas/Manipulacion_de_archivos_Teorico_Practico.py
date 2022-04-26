# Manipulacion de archivos Teorico-Practico
# Desafio 1
#  Creá un archivo de prueba (bio.txt) en la carpeta destinada a los prácticos de la materia.
with open("C:\Users\mateo\Documents\GitHub\Funadmentos-de-Informatica--Comision-B\Practicas\bio.txt", "w") as archivo:
    archivo.read()
#Desafio 2
#Investigá sobre los métodos os.mkdir() y os.listdir()
"""
La funcion os.mkdir crea un directorio en blanco en el sistema de archivos
La funcion os.listdir lista los archivos y directorios en el sistema de archivos.
"""

#Desafio 3
#Abrí el archivo bio.txt y escribí una mini biografía de presentación. 
with open("C:\Users\mateo\Documents\GitHub\Funadmentos-de-Informatica--Comision-B\Practicas\bio.txt", "w") as archivo:
    archivo.write("Mini biografia de presentacion")

#Desafio 4
#Descargá el archivo manipulacion_archivos.txt y creá un programa que lea su contenido y lo imprima en pantalla el resultado.
with open("C:\Users\mateo\Desktop\UCEMA\2año\1Cuatrimestre\Fundamentos_de_informatica\Fundamentos_de_informatica\Python_intro\manipulacion_archivos.txt", "r") as archivo:
    print(archivo.read())