#Ejercicio 1
def lineadearchivo(archivo, letra):
    """
    Funcion que lee un archivo y dice cuantas lineas empiezan con n letra
    """
    with open(archivo, "r") as f:
        contador = 0
        linea = f.readline()
        if linea[0] == letra:
            contador += 1        
        return contador

#Ejercicio 2
def imprimirlineas(archivo, n):
    """
    Funcion que lee un archivo y imprime las n primeras lineas
    """
    with open(archivo, "r") as f:
        for i in range(n):
            print(f.readline())

#Ejercicio 4
def cuantaspalabrasarchivo(archivo):
    """
    Leer archivo y cuantas palabras tiene
    """
    with open(archivo, "r") as f:
        linea = f.readline()
        palabras = linea.split()
        return len(palabras)

#Ejercicio 7
def maslarga(archivo):
    """
    Leer archivo y palabra mas larga
    """
    with open(archivo, 'r') as f:
        palabras = f.read().split()
        maslarga = max(palabras, key=len)
    return print(maslarga), print(len(maslarga))

#Ejercicio 8
def Joinfiles(file1, file2, file3):
    """
    Junta dos archivos en uno nuevo
    """
    with open(file1, "r") as f1, open(file2, "r") as f2, open(file3, "a") as f3:
        f3.write(f1.read() + f2.read())
Joinfiles("Docuemento 1", "Documento 2", "Documento 3")

#Ejercicio 9
def frecuencia_palabra(archivo, palabra):
    with open(archivo) as f:
        linea = f.readline()
        palabras = linea.split()
        contador = 0
        for i in range(len(palabras)):
            if palabras[i] == palabra:
                contador += 1
        return contador/len(palabras)




