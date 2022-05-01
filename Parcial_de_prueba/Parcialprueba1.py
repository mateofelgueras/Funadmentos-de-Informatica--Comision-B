#Cosigna 1
def aparece_string(cadena):
    
 #   Función que determina si una cadena aparece en otra.
    
    import re
    print(len(re.findall("bc9", cadena)))

def partedestringquenocontengacenelmedio(cadena):
    import re
    print((re.findall(r"aa([^c].*?)gg", cadena)))
    

#Cosigna 2
class Auto:
    def __init__(self):
        self.consumo = 0.05 
        self.rpm = 0
        self.cambio = 0

    def arrancar(self):
        self.cambio += 1
        self.rpm += 500

    def subirCambio(self):
        if self.cambio <5:
            self.cambio += 1
        else:
            print("No puede subir el cambio")

    
    def bajarCambio(self):
        if 0<self.cambio <=5:
            self.cambio -= 1
        else:
            print("No puede bajar el cambio") 
    
    def subirRPM(self, rpm):
        if (self.rpm +rpm) <= 5000:
            self.rpm += rpm
        else:
            self.rpm = 5000
    
    def bajarRPM(self, rpm):
        if  (self.rpm - rpm) >=0:
            self.rpm -= rpm
        else:
            self.rpm =0    

    def velocidad(self):
        return (self.rpm/100) *(0.5 + self.cambio/2)
    
    def consumoActualPorKm(self):
        if self.rpm > 3000:
            if self.cambio == 1:
                return self.consumo * 3 * ((self.rpm - 2500)/500)
            if self.cambio == 2:
                return self.consumo * 2 * ((self.rpm - 2500)/500)
            if self.cambio >= 3:
                return self.consumo * 1 * ((self.rpm - 2500)/500)
        elif self.cambio == 1:
            return self.consumo * 3
        elif self.cambio == 2:
            return self.consumo * 2
        else:
            return self.consumo

#Ejercicio3

#Es un error de Division por cero

muestras_2 = ["d"]

def obtener_media(lista):
    sumatoria = 0
    try:

        for valor in lista:
            sumatoria += valor
        longitud = len(lista)

        return sumatoria / longitud
    except ZeroDivisionError:
        print("Error de división por cero")
    except TypeError:
        print("Solo numeros permitidos")
obtener_media(muestras_2)

#Ejercicio 4
import os
from posixpath import abspath, relpath
import shutil
os.mkdir("Resultado")
path = os.getcwd()
lista = os.listdir(path)
for i in lista:
    if i.endswith(".txt"):
        with open("texto_completo.txt", "a") as f:
            with open(i, "r") as g:
                f.write(g.read())

shutil.move("texto_completo.txt", "Resultado/texto_completo.txt")
