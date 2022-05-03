
#Ejercicio 1
print("palabra que queres saber el largo")
palabra = input()
print(len(palabra))

#Ejercicio 2
print('palabra que queres')
palabra = input()
print(str.upper(palabra[4])) 
print(str.upper(palabra[5]))


#Ejercicio 3
print("Cual es tu nombre y apellido?")
nombre = input()
print("Hola "+nombre)

#Ejercicio 4
nombre = (input("Nombre: "))
apellido1 = (input("Primer apellido: "))
apellido2 = (input("Segundo apellido: "))
print(str.upper(nombre[0] + apellido1[0] + apellido2[0]))

#Ejercicio 5
numero1 = int(input("Dígame un número: "))
numero2 = int(input("Dígame otro número: "))
numero3 = int(input("Digame otro numero: "))
print((numero1 + numero2 + numero3)/3)

#Ejercicio 6
Datos = int(input("Minutos: "))
hora= Datos//60
minutos= Datos - (hora* 60)
print("Horas:", hora,"Minutos:", minutos)

#Ejercicio 7
def comision(sueldo_base, ventas):
    return ((sueldo_base*0.1)*ventas)

def ganancia(sueldo_base, ventas):
    return print("sueldo total:",(sueldo_base + comision(sueldo_base, ventas)),"Comisiones", comision(sueldo_base, ventas))
    
#Ejercio 8
def nota_final(correctas, incorrectas):
    return print("nota final:", correctas*4-incorrectas*1)
    
"""Ejercicio 9
costo_total= int(input("Costo de la casa:"))
porcentaje_sueldo= float(input(f"Que porcentaje de sueldo quiere ahorrar por mes:"))
sueldo_anual=int(input(f"Cual es su sueldo anual:"))
cantidad_ahorro= 0
deposito=costo_total*0.25
cantidad_ahorro_mes=(sueldo_anual/12)*porcentaje_sueldo
print(deposito/cantidad_ahorro_mes)"""

