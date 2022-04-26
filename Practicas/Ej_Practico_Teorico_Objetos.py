#Clase AnimalesAlados que hereda a Golondrina y Dragon.
class AnimalesAlados:
  def esta_feliz(self):
    return self.energia > 500

class Golondrina(AnimalesAlados):
  def __init__(self, energia):
    self.energia = energia

  def comer_alpiste(self, gramos):
    self.energia += 4 * gramos

  def volar_en_circulos(self):
    self.volar(0)

  def volar(self, kms):
    self.energia -= 10 + kms
#Funciones esta_debil y  esta_feliz agregadas.
  def esta_debil(self):
    return self.energia < 10

pepita=Golondrina(100)
anastasia = Golondrina(200)
maria = Golondrina(42)

class Dragon(AnimalesAlados):     
  def __init__(self, cantidad_dientes, energia):
    self.energia = energia
    self.cantidad_dientes = cantidad_dientes

  def escupir_fuego(self):
    self.energia -= 2 * self.cantidad_dientes

  def comer_peces(self, unidades):
    self.energia += 100 * unidades

  def volar_en_circulos(self):
    self.energia -= 1

  def volar(self, kms):
    self.energia -= 10 + kms/10
#Funciones esta_debil agregada. 
  def esta_debil(self):
    return self.energia < 50

#Creo clase Entrenador
class Entrenador:
  def _init_(self, equipo):
    self.equipo = equipo

  def el_equipo(self):
    return self.equipo

  def agregar_animal(self, dragon):
    self.equipo.append(dragon)
 
  def entrenar_dragon(self, dragon):
    for i in range(20):
      dragon.volar_en_circulos()
    dragon.comer_peces(3)

  def entrenar_equipo(self):
    for dragon in self.equipo:
      self.entrenar_dragon
  
  def entrenamiento_intensivo(self):
    for dragon in self.equipo:
      while dragon.esta_debil == False:
        dragon.volar_en_circulos()
       

r

roberta = Dragon(10, 1000)
chimuelo = Dragon(200, 1000)
hipo = Entrenador([roberta])