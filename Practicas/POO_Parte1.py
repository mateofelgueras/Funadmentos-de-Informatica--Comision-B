#Ejercicio 1
"""
Estado: El estado de un objeto es el cojunto de atributos del objeto. En este caso, el estado es self o alimento y caricias.
Interfaz: La interfaz de un objeto es el conjunto de mensajes que cada objeto expone. En este caso seria energia, comer, acariciar, esta debil.
"""
#Ejercicio 2
def volar(self, kms):
    if self.energia >0:
        self.energia -= 10 + kms/10
    else:
        print("No puede volar")

#Ejercicio 3
class Notebook:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio

    def descuento_precio(self, porcentaje):
        self.precio = self.precio - (self.precio * porcentaje / 100)
#Ejercicio 4
class Contador:
    def __init__(self, valor_inicial):
        self.valor_inicial = valor_inicial
    
    def inc(self):
        self.valor_inicial += 1
    
    def dis(self):
        self.valor_inicial -= 1
    
    def reset(self):
        self.valor_inicial = 0
    
    def valorNuevo(self, valor_nuevo):
        self.valor_inicial = valor_nuevo

    def valorActual(self):
        return self.valor_inicial

#Ejercicio 5
class Contador:
    def __init__(self, valor_inicial):
        self.valor_inicial = valor_inicial
    
    def inc(self):
        self.valor_inicial += 1
        lista1.append(self.valor_inicial)
    
    def dis(self):
        self.valor_inicial -= 1
    
    def reset(self):
        self.valor_inicial = 0
    
    def valorNuevo(self, valor_nuevo):
        self.valor_inicial = valor_nuevo

    def valorActual(self):
        return self.valor_inicial
    
    def ultimoComadando(self):
        return lista1[-1]
        