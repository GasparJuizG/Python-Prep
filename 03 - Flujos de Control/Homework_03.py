# 1)

valor = 3

if valor == 0:
    print("igual a cero")

elif valor >> 0:
    print("mayor a cero")

elif valor << 0:
    print("menor a cero")

# 2)

'''valor2 = input("ingrese dato ")

if type(valor) == type(valor2):
    print("son del mismo tipo")

else:
    print("no son del mismo tipo")'''

# 3)

for i in range (0,20):
    numero = i + 1
    if (int(numero / 2) == float(numero / 2)):
        print(f"{numero} es par")
    elif (int(numero / 2) != float(numero / 2)):
        print(f"{numero} es impar")

# 4)

for i in range(0,6):
    print(i**3)

# 5)

valor3 = 5
juan = 0
for i in range (valor3):
    juan += 1
    print(juan)

# 6)

valor6 = 6
if valor6 != 0:
    itera = 1
    operador = valor6
    factorial = 1
    while itera < valor6:
        itera += 1
        factorial *= operador
        operador -= 1
    print(factorial)

# 9)
print("1 es primo")
for i in range(2,31):
    itera = 1
    primo = 0
    while itera < i:
        if int(i / itera) == float(i / itera) and itera != 1:
            primo = 1
            itera = i
        else:
            itera += 1
    if primo == 0:
        print(f"{i} es primo")    