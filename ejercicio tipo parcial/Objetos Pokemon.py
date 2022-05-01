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
         self.nombre + "" + self.nombre


 
# a) ¿Cuál es el nombre de la clase? ¿Cuál es el estado de un Pokemón? ¿Qué mensajes entiende un Pokemon? 
# el nombre de la clase es 'pokemon'
"""
    El nombre de la clase es Pokemon
    El estado de un pokemon es vidas, nombre, nivel
    Los mensajes que entiende un pokemon son: pelear, entrar_pokebola, comer, beso_drenaje, saludar
    """
     #el estado de un pokemon se define por: la vida (que arranca en 10), despues por su nombre y por ultimo el nivel (que arranca en 1). todo esto dependiendo de si le pido que pelee, que entre a una pokebola o que coma. todo eso va a variar dependiendo de lo que le digas que haga.
     #un pokemon entiende por ejemplo: 
     
    poke = Pokemon(5, 'sylveon',2)

    poke.pelear()  #el pokemon pierde 3 de vida
    poke.comer() # el pokemon gana 5 de vida
    poke.entrar_pokebola()     #el pokemon gana 2 de vida

  # b) Instanciá al Pokemón Sylveon.
   sylveon = Pokemon
   
   #c) Definir el método beso_drenaje que le otorga 5 vidas, ya que drena la energía de su oponente.
   #(lo hago arriba)
   
  # d) Definir un método saludar que retorne el nombre del Pokemon por duplicado.
    # (lo hago arriba)