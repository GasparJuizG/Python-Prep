class Grados:
    def __init__(self,valor,unidad):
        self.valor = valor
        self.unidad = unidad
        pass
    
    def conversion(self):
        unidad1 = input("ingrese unidad a la que se quiere convertir (ej: °F) ")
        conv = 0
        if self.unidad == "°C" and unidad1 == "°F":
            conv = float(9/5 * self.valor + 32)
        elif self.unidad == "°F" and unidad1 == "°C":
            conv = float((self.valor - 32)/(9/5))
        elif self.unidad == "°C" and unidad1 == "°K":
            conv = float(self.valor + 273)
        elif self.unidad == "°K" and unidad1 == "°C":
            conv = float(self.valor - 273)
        elif self.unidad == "°K" and unidad1 == "°F":
            conv = float(9/5 * (self.valor - 273) + 32)
        elif self.unidad == "°F" and unidad1 == "°K":
            conv = float(((self.valor - 32)/(9/5)) + 273)
        return conv

    def factorial(self):
        fact = 1
        if self.valor < 0 or int(self.valor) != float(self.valor):
            self.valor = int(input("no se puede realizar la operacion, ingrese un numero entero positivo: "))
        if self.valor >= 0 and int(self.valor) == float(self.valor):
            for i in range(self.valor):
                fact *= (self.valor - i)
        return fact