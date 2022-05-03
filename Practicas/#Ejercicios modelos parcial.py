#Ejercicios modelos parcial
class Titan:
    def __init__(self, vida):
        self.vida = vida
    
    def recibir_ataque(self,danio):
        self.vida -= danio*1.5

    def esta_vivo(self):
        return self.vida > 0
    
    def salud_actual(self):
        return self.vida
    
    def cuantas_casas(self):
        return self.vida *8/100
    
    def grito(self):
        return "Aaaarrrg"

titan1 = Titan(100)
titan1.recibir_ataque(30)
print(titan1.esta_vivo())
print(titan1.salud_actual())
print(titan1.cuantas_casas())
print(titan1.grito())
titan1.destruir_casas()
titan1.salud_actual()
titan1.recibir_ataque(4)
print(titan1.esta_vivo())