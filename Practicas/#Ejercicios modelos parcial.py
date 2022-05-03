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
titan1.salud_actual()
titan1.recibir_ataque(4)
print(titan1.esta_vivo())

"""True
55
4.4
"¡Aaaarrrg!"
5.0
False"""

class Enterprise:
    def __init__(self,):
        self.potencia = 50
        self.coraza = 5
    
    def encontrarPilaAtomica(self):
        if self.potencia + 25 > 100:
            self.potencia = 100
        else:
            self.potencia += 25
    
    def encontrarEscudo(self):
        if self.coraza + 10 > 20:
            self.coraza = 20
        else:
            self.coraza += 10
    
    def recibirAtaque(self, cantidad):
        if self.coraza - cantidad < 0:
            if self.potencia - (cantidad - self.coraza) < 0:
                self.potencia = 0
                self.coraza = 0
            else:
                self.potencia -= (cantidad - self.coraza)
                self.coraza = 0
    
    def fortalezaDefensiva(self):
        return self.coraza + self.potencia
    
    def necesitaFortalecerse(self):
        return self.potencia < 20 and self.coraza == 0
    
    def fortalezaOfensiva(self):
        if self.potencia < 20:
            return 0
        else:
            return (self.potencia - 20) / 2
            
enterprise = Enterprise()
enterprise.encontrarPilaAtomica()
enterprise.recibirAtaque(14)
enterprise.encontrarEscudo()
print(enterprise.potencia)
print(enterprise.coraza)
"""
66
10
"""

class Estudiante:
    def __init__(self, energia):
        self.energia = energia
        self.estado = False
    
    def energia_actual(self):
        return self.energia
    
    def dormir(self, horas):
        if self.energia + (horas * 100/8) > 100:
            self.energia = 100
        else:
            self.energia += horas * 100/8
    
    def comer(self):
        self.energia += 10
    
    def hacer_ejercicio(self, minutos):
        if self.energia - minutos *25/30 < 0:
            self.energia = 0
        else:
            self.energia -= minutos*25/30
    
    def esta_feliz(self):
        return self.estado
    
    def estudiar(self, hora):
        if self.energia - hora *20 < 0:
            self.energia = 0
        else:
            self.energia -= hora*20
    
    def aprobar(self):
        self.estado = True
        return self.estado

estudiante = Estudiante(100)
estudiante.hacer_ejercicio(30)
estudiante.estudiar(3)
estudiante.comer()
print(estudiante.aprobar())
print(estudiante.energia_actual())

"""
True
25.0
"""