# La entrega del examen se hará por este medio: tendrás que confeccionar el código adecuado para realizar cada actividad, generar los archivos correspondientes en el caso deser necesario y pushearlos a este repo que se te generó automáticamente.

# Las devoluciones de este examen se harán por GitHub Classroom, por medio de Issues y comentarios. Debés hacer un commit cada 5 min, de lo contrario tu entrega no será considerada válida. En todo momento debés estar conectado al zoom, con la cámara prendida.

# Consigna N°1
# Escribir funciones que, dado un String, permitan obtener

#  - cuántas veces aparece el string bc9. P.ej. aparece 2 veces en xsabc9cabcb3sabc9, y ninguna en hola amigos mios.
#  - la lista de los substrings delimitados entre ‘aa’ y ‘gg’, que no incluyan ninguna ‘c’. P.ej. en ‘ttaatatggttaacatgg’, debe tomar solamente ‘tat’, rechazando ‘cat’.

def cuantas_veces_aparece(string):
        return string.count('bc9')

def cuantas_veces_aparece(string):
    import re
    return len(re.findall(r'bc9', string))

def lista_substrings_que_esten_entre_letras(string):
    import re
    return re.findall(r'aa([^c]*?)gg', string)

# Consigna N°2

# *A)* Dado la siguiente clase respondé: ¿Cuál es el nombre de la clase? ¿Cuál es su estado? ¿Qué mensajes entiende el Avatar? 
"""
El nombre de la clase es 'Avatar', el estado de un avatar es energia, elementos, mascota. Su interfaz o mensajes son los siguientes: estado_avatar, meditar, comer
"""

# Python
class Avatar:
    def __init__(self, mascota):
        self.mascota = mascota
        self.energia = 10
        self.elementos = []
     
    def estado_avatar(self):
         self.energia -= 8

    def meditar(self):
 	    self.energia += 1



 

"""*B)* Vamos a modelar de manera muy simple la mecánica de un nuevo juego Sonic. Como sabemos Sonic acumula puntos (matando enemigos),
 anillos y vidas, pero en este nuevo juego también tiene energía (la cual empieza en 100, que es la energía máxima)
 y solo existe un tipo de enemigo con distintas variaciones a las cuales vamos a llamar XS, S, M, L y XL (si, como los talles de ropa) 
 dependiendo de la dificultad que representan (cuantos golpes se necesitan para matarlos). Por cada golpe que da, Sonic pierde energía,
  la cual le toma un tiempo recuperar, por lo que no puede dar más de 3 golpes seguidos y es más vulnerable a ataques de enemigos. 
  Considerando todo esto Sonic tiene que entender los mensajes:"""

#  - *agarrarAnillo(cantidad)*, el cual aumenta en cierta cantidad los anillos que tiene Sonic.
#  - *darGolpe()* el cual disminuye en un 30% del total la energía de Sonic. En el caso de no tener la energía necesaria debe aparecer un cartel que diga esto.
#  - *recuperarEnergia(tiempo)* el cual recupera energía desde 10 hasta los 100 puntos en 10 segundos (recupera proporcionalmente si el tiempo es menor y recupera hasta 100 si el tiempo es mayor a 10).
#  - *matarEnemigo(enemigo)* el cual disminuye la energía dependiendo del enemigo y en caso de quedarse con menos energía de la que necesita Sonic pierde el 10% de los anillos (consideramos que Sonic siempre ataca cuando tiene la energía al máximo). 
# Al matar al enemigo gana una cantidad de puntos correspondiente al enemigo (XS: 20 puntos, S: 35 puntos, M: 50 puntos, L: 65 puntos, XL: 80 puntos).

# Definí las clases *Sonic* y *Enemigo* e instancialas (un enemigo S y uno XL) y ejecutá las siguientes líneas:
class Sonic:
    def __init__(self):
        self.energia = 100
        self.puntos = 0
        self.anillos = 0
        self.vidas = 0
    
    def agarrarAnillos(self, cantidad):
        self.anillos += cantidad
    
    def darGolpe(self, cantidad):
        if cantidad > 3:
            print("Sonic no puede golpear mas de 3 veces seguidas")
        elif self.energia - 30 * cantidad < 0:
            print("Sonic no tiene energia suficiente para dar golpes")
        else:
            self.energia -= 30 * cantidad
    
    def recuperarEnergia(self, tiempo):
        if tiempo >= 10:
            self.energia = 100
        elif self.energia + tiempo * 9 > 100:
            self.energia = 100
        elif self.energia + tiempo * 9 <= 100:
            self.energia += tiempo * 9
        
    def matarEnemigo(self, enemigo):
        if 60 < enemigo.energia <= 80:
            self.darGolpe(3)
            self.puntos += enemigo.energia
            if self.energia < enemigo.energia:
                self.anillos=self.anillos * 0.1
                self.energia = 0
        elif 30 < enemigo.energia <= 60:
            self.darGolpe(2)
            self.puntos += enemigo.energia
            if self.energia < enemigo.energia:
                self.anillos = self.anillos* 0.1
                self.energia = 0
        elif enemigo.energia <= 30:
            self.darGolpe(1)
            self.puntos += enemigo.energia
            if self.energia < enemigo.energia:
                self.anillos = self.anillos* 0.1
                self.energia =0

class SonicMejorado(Sonic):
    def energiaPorAnillos(self, cantidadAnillos):
        self.energia += cantidadAnillos * 0.2

class Enemigo:
    def __init__(self, energia):
        self.energia = energia


t = Enemigo(80)
r = Enemigo(30)
sonico = SonicMejorado()

# python
#sonic.agarrarAnillos(50)
# sonic.matarEnemigo(enemigoS)
# print(sonic.anillos)
# print(sonic.energia)
# sonic.recuperarEnergia(10)
# print(sonic.energia)
# sonic.matarEnemigo(enemigoXL)
# print(sonic.anillos)
# print(sonic.energia)
# sonic.recuperarEnergia(5)
# print(sonic.energia)
# 

# El resultado de esto debería ser:

# 	50
# 	70
# 	100
# 	5.0
# 	0
# 	45.0

# *C)* A medida que avanza el juego Sonic obtiene nuevas habilidades tales como recuperar energía agarrando anillos
#  de manera que recupera 0.2 unidades de energía por cada anillo que agarra. Definí la clase *SonicMejorado* que 
# herede de *Sonic* y que además entienda el mensaje *energiaPorAnillos(cantidadAnillos)* el cual recupere 
# la energía de Sonic como está definido más arriba.
class SonicMejorado(Sonic):
    def energiaPorAnillos(self, cantidadAnillos):
        self.energia += cantidadAnillos * 0.2

# Ejecutando las siguientes líneas (eliminando la ejecución del inciso *B*):

# python
# sonicMejorado.agarrarAnillos(50)
# sonicMejorado.matarEnemigo(enemigoS)
# print(sonicMejorado.anillos)
# print(sonicMejorado.energia)
# sonicMejorado.recuperarEnergia(10)
# print(sonicMejorado.energia)
# sonicMejorado.matarEnemigo(enemigoXL)
# print(sonicMejorado.anillos)
# print(sonicMejorado.energia)
# sonicMejorado.recuperarEnergia(5)
# print(sonicMejorado.energia)
# sonicMejorado.energiaPorAnillos(50)
# print(sonicMejorado.energia)
# 

# El resultado de esto debería ser:
	
# 	50
# 	70
# 	100
# 	5.0
# 	0
# 	45.0
# 	55.0


