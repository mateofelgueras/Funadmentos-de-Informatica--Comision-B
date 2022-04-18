#Ejercicio 1
def lineadearchivo(archivo, letra):
    with open(archivo) as f:
        linea = f.readline()
        return linea

#Ejercicio 2
def imprimirnlineas(archivo, n):
    with open(archivo) as f:
        for i in range(n):
            linea = f.readline()
            print(linea)

#Ejercicio 4
def cuantaspalabrasarchivo(archivo):
    with open(archivo) as f:
        linea = f.readline()
        palabras = linea.split()
        return len(palabras)

#Ejercicio 7
def def maslarga(archivo):
    """
    Funcion que lee un archivo y devuelve la palabra mas larga
    """
    with open(archivo, 'r') as f:
        palabras = f.read().split()
        maslarga = max(palabras, key=len)
    return print(maslarga), print(len(maslarga))

#Ejercicio 9
def frecuenciadecadapalabra(archivo, palabra):
    with open(archivo) as f:
        linea = f.readline()
        palabras = linea.split()
        contador = 0
        for i in range(len(palabras)):
            if palabras[i] == palabra:
                contador += 1
        return contador/len(palabras)

