#Ejercicio 1 
"""
Estados: alimento y caricias
Interfaz Perro: energia, comer, acariciar, esta debil, pasear
Interfaz Gato: energia, comer, acariciar, esta debil
Comparten interfaz parcialmente

"""
#Ejercicio 2
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

  def esta_debil(self):
    return self.energia < 10

  def esta_en_equilibrio(self):
    return 150 < self.energia <300

class Ornitologo:
    def __init__(self, aves):
        self.aves=aves
    
    def estudiar_ave(self, ave):
        self.aves.append(ave)
    
    def aves_en_estudio(self):
        print(self.aves)
    
    def realizarRutinaSobreAves(self):
        for ave in self.aves:
            ave.comer_alpiste(80)
            ave.volar(70)
            ave.comer_alpiste(10)
    
    def avesEnEquilibrio(self):
        en_equi = []
        for ave in self.aves:
            if ave.esta_en_equilibrio():
                en_equi.append(ave)
        print(en_equi)

#Ejercicio 4
class MedioDeTransporte:
    def __init__(self, combustible):
        self.combustible = combustible
    
    def cargar_combustible(self, cantidad):
        self.combustible += cantidad
    
    def entran_personas(self, cantidad):
        return cantidad <= self.maximo_personas()

class Moto(MedioDeTransporte):
    def recorrer(self, kms):
        self.combustible -= kms
    
    def maximo_personas(self):
        return 2
    
class Auto(MedioDeTransporte):
    def recorrer(self, kms):
        self.combustible -= 0.5*kms

    def maximo_personas(self):
        return 5


