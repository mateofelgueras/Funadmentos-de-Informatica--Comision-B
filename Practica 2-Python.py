"""Ejercicio 1
cadena=(input("palabra: "))
if cadena[0] == str.upper(cadena[0]):
    print("Es mayuscula") 
else:
    print("Es minuscula") """

"""Ejericicio 2 
def par_impar(numero):
    if numero % 2 == 0:
      print("Es par")
    else:
        print ("Es impar")
numero = int(input("Numero: "))
if numero>0:
    print("Es positivo",par_impar(numero))
elif numero<0:
    print("Es negativo",par_impar(numero))
else:
    print("El numero es 0",par_impar(numero))"""

"""Ejercicio 3
def cara_dado(numero):
    if numero==1:
        print("6")
    elif numero==2:
        print("5")
    elif numero ==3:
        print("4")
    elif numero==4:
        print("3")
    elif numero==5:
        print("2")
    elif numero==6:
        print("1")
    else:
        print("Numero incorrecto ingresado, tiene que ser del 1 al 6")
numero=int(input("Numero: "))
print(cara_dado(numero))"""

"""Ejercicio 4
def costo_translado(zona, peso_gr):
    if peso_gr >= 5000:
        return "No hacemos envios por ese peso"
    elif zona==1:
        return peso_gr*10
    elif zona==2:
        return peso_gr*15
    elif zona==3:
        return peso_gr*18
    elif zona==4:
        return peso_gr*24
    elif zona==5:
        return peso_gr*30
zona=int(input("A que zona es:"))
peso_gr=int(input(f"Peso en gramos: "))
print("El costo del translado es de $"+str(costo_translado(zona, peso_gr)))"""

"""Ejercicio 5
semana= ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
numero=int(input("Escribir numero: "))
if 1 <= numero <=7:
    print(semana[numero-1])
else:
    print("El numero ingresado no es valido")"""

"""Ejercicio 6
lista1=[input(), input(), input()]
lista2=lista1.reverse()
print(lista1)"""

"""Ejercicio 7
lista=[]
numero =int(input("Ingrese numero:"))
while numero>=0:
    lista.append(numero)
    numero =int(input("Ingrese numero:"))
if numero<0:
    print(lista)"""

"""Ejercicio 8

lista1=[int(input()), int(input()), int(input()), int(input()), int(input())]
lista2=[int(input()), int(input()), int(input()), int(input()), int(input())]
lista3=[lista1[0]+lista2[0], lista1[1]+lista2[1], lista1[2]+lista2[2],lista1[3]+lista2[3],lista1[4]+lista2[4]]
print(lista3)"""

"""Ejercicio 12 
cantidad = int(input("Introducir cantidad de alumnos:"))
alumnos = {}

for num in range(0, cantidad):
    alumno = input("alumno: ")
    notas = []
    nota =int(input("nota: "))

    while nota >= 0:
        notas.append(nota)
        nota= int(input("nota: "))
    alumnos[alumno] = notas

for alumno in alumnos:
    print(alumno, sum(alumnos[alumno])/len(alumnos[alumno]))"""


