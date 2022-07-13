from math import factorial


class Vehiculo:
    def __init__(self,tipo,color,cilindrada,velocidad,direccion):
        self.tipo = tipo
        self.color = color
        self.cilindrada = cilindrada
        self.velocidad = velocidad
        self.direccion = direccion
        pass

    def acelerar(self):
        self.velocidad += 10
        pass

    def frenar(self):
        self.velocidad -= 10
        pass

    def doblar(self):
        self.direccion = "doblando"
        pass

    def estado(self):
        print(f"la velocidad es de {self.velocidad} y esta {self.direccion}")

    def describe(self):
        print(f"es del tipo {self.tipo}, del color {self.color} y de cilindrada {self.cilindrada}")

v1 = Vehiculo("Auto","Rojo","1.8",40,"yendo recto")
v2 = Vehiculo("moto","verde","0.8",40,"yendo recto")
v3 = Vehiculo("camion","blanco","4.0",40,"yendo recto")



import sys
sys.path.append(r'/Users/gaspi/Desktop/Data Science/Python-Prep/07 - Classes & OOP/Tools.py')

import Tools

grados1 = Grados(200, "°K")
grados1.conversion()
