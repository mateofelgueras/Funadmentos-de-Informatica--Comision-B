#Escribir una función que, dado un String, permita validar si este se corresponde o no con un teléfono de CABA.
import re

def telefono_caba(string):
    print(bool(re.match(r'[+](54)(9?)(11)(\d{8}$)', string)))

#bool --> retorna True or False
#match --> casi lo mismo que search --> solo que busca en la primer palabra
# r -->siempre en re para que lea el string
#[+] --> porque es un metacaracter
#(9?) --> puede variar si esta o no
# (\d) --> numero
#{8} --> que sean 8 numeros mas, ni mas ni menos
#$ --> fin de linea
