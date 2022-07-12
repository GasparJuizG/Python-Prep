# 1)
from calendar import c


numero = 13
def primo(num):
    prim = True
    for i in range(2,num):
        if int(num/i) == float(num/i):
            prim = False
            return prim
            break
    if prim == True:
        return prim

# 2)
numeros = [1,2,3,4,5,6,7,893,765]

def primos(lista):
    listaPrimos = []
    for i in lista:
        if primo(i) == True:
            listaPrimos.append(i)
    return listaPrimos

print(primos(numeros))

# 3)
numeros = [1,1,1,2,2,3,3,45,5,6,7,7,7,7,7,4,2,3,1,2,3,4,5,6]

def repetidos(lista,string):
    tuple = (0,0)
    for i in lista:
        cant = lista.count(i)
        if cant >= tuple[1]:
            tuple = (i,cant)
    return tuple

# 4)
parametro = "mayor"
def repetidos(lista,string):
    if string == "mayor": 
        tuple = (0,0)   
        for i in lista:
            cant = lista.count(i)
            if cant >= tuple[1]:
               tuple = (i,cant)
        return tuple
    if string == "menor":
        tuple = (999999999999,999999999999)    
        for i in lista:
            cant = lista.count(i)
            if cant <= tuple[1]:
               tuple = (i,cant)
        return tuple

# 5)
value = 100
un0 = "°K"
un1 = "°C"

def conversion(valor,unidad0,unidad1):
    conv = 0
    if unidad0 == "°C" and unidad1 == "°F":
        conv = float(9/5 * value + 32)
    elif unidad0 == "°F" and unidad1 == "°C":
        conv = float((value-32)/(9/5))
    elif unidad0 == "°C" and unidad1 == "°K":
        conv = float(value + 273)
    elif unidad0 == "°K" and unidad1 == "°C":
        conv = float(value - 273)
    elif unidad0 == "°K" and unidad1 == "°F":
        conv = float(9/5 * (value - 273) + 32)
    elif unidad0 == "°F" and unidad1 == "°K":
        conv = float(((value - 32)/(9/5)) + 273)
    return conv


# 6)
temperaturas = [(100,"°K","°C"),(300,"°F","°C"),(350,"°C","°K")]
for i in temperaturas:
    value, un0, un1 = i
    print(conversion(value,un0,un1))

# 7)
numero = 6.5
def factorial(num):
    fact = 1
    if num < 0 or int(num) != float(num):
        num = int(input("por favor, ingrese un valor entero positivo "))
    if num >= 0 and int(num) == float(num):
        for i in range(num):
            fact *= (num - i)
    return fact
print(factorial(numero))




