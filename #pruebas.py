#pruebas
muestras_2 = ["d"]

def obtener_media(lista):
    sumatoria = 0
    try:

        for valor in lista:
            sumatoria += valor
        longitud = len(lista)
        try:
            return sumatoria / longitud
        except ZeroDivisionError:
            print("Error de división por cero")
    except TypeError:
        print("Solo numeros permitidos")