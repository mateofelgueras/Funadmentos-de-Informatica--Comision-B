# Primer_parcial_FI2A
#La entrega del examen se hará por este medio: tendrás que confeccionar el código adecuado para realizar cada actividad, generar los archivos correspondientes en el caso de ser necesario y pushearlos a este repo que se te generó automáticamente. 

#Las devoluciones de este examen se harán por GitHub Classroom, por medio de Issues y comentarios. *Debés hacer un commit cada 5 min, de lo contrario tu entrega no será considerada válida. En todo momento debés estar conectado al zoom, con la cámara prendida.*  

### Consigna N°1
#Dada la siguiente clase resolvé los siguientes ejercicios y respondé las preguntas:
 # Python
class Pokemon():
     def __init__(self, vidas = 10, nombre, nivel = 1):
        self.vidas = vidas
        self.nombre = nombre
        self.nivel = nivel
     
     def pelear(self):
        self.vidas -= 3
        
     def entrar_pokebola(self, entrenador):
        self.vidas += 2
     
     def comer(self):
        self.vidas += 5
    
     def beso_drenaje(self):
        self.vidas += 5

     def saludar(self):
        return self.nombre + "" + self.nombre 
  
  # a) ¿Cuál es el nombre de la clase? ¿Cuál es el estado de un Pokemón? ¿Qué mensajes entiende un Pokemon? 
"""
  El nombre de la clase es Pokkemon, el estado es vidas nombre nivel y los mensjaes son pelaer, entrar_pokebola, comer.
"""
#b) Instanciá al Pokemón Sylveon.
sylveon = Pokemon()
   
  # c) Definir el método beso_drenaje que le otorga 5 vidas, ya que drena la energía de su oponente.
   
  # d) Definir un método saludar que retorne el nombre del Pokemon por duplicado.



### Consigna N°3
#Escribir una función que, dado un String, permita validar si este se corresponde o no a una fecha (con formato día, mes, año).
def validar_si_es_fecha(string):
    import re
    re.match(r'\d{2}/\d{2}/\d{4}', string)
        


### Consigna N°4
#En un mundo distópico la humanidad es atacada sin descanso por titanes. Estos titanes son muy resistentes pero no inmortales, su salud (100 de máxima)
#  puede ir disminuyendo si reciben daño debido a algún ataque, y si llega a 0 se muere.
#Al recibir este ataque la salud disminuye 1.5 por cada puntos de daño recibido. Además tienen la capacidad de destruir cierto
#  número de casas dependiendo de su salud, siendo 6 casas cuando su salud es máxima o un número proporcional si su salud es
#  menor a la máxima (si tiene 60 puntos de salud destruiría 3.6 casas, es decir, 3 casas completas y más de la mitad de otra). 
# Sin embargo no tienen la capacidad de comunicarse con los humanos, siendo un grito, "¡Aaaarrrg!", el único sonido que hacen. 
# Pero para empeorar las cosas existen súper titanes, los cuales tienen la capacidad de correr y regenerarse la salud (20 puntos cada 15 minutos).
#Definí las clases Titan y Supertitan con los atributos y métodos correspondientes y hacé que esta última herede de la primera.
#  Además instanciá a dos Supertitanes y ejecutá las siguientes líneas:

class Titan:
      def __init__(self):
         self.vida = 100
      
      def recibir_ataque(self, cantidad_de_ataque):
         self.vida -= cantidad_de_ataque*1.5
      
      def cuantas_casas(self):
         return 6 * self.vida / 100
      
      def salud_actual(self):
         return self.vida
      
      def esta_vivo(self):
         return self.vida > 0
      
      def grito(self):
         return "Aaaarrrg!"

class Supertitan(Titan):
      def recuperarse(self, minutos):
         self.vida += 20 * minutos / 15


#python

supertitan1 = Supertitan(100)
supertitan1.recibir_ataque(40)
print(supertitan1.salud_actual())
print(supertitan1.cuantas_casas())
print(supertitan1.esta_vivo())
print("\n")
supertitan2 = Supertitan(70)
print(supertitan2.grito())
supertitan2.recibir_ataque(30)
print(supertitan2.cuantas_casas())
supertitan2.recuperarse(15)
print(supertitan2.salud_actual())
supertitan2.recibir_ataque(30)
print(supertitan2.esta_vivo())


#cuyo resultado tiene que ser:

python
#40.0
#2.4
#True


#¡Aaaarrrg!
#1.5
#45.0
#False