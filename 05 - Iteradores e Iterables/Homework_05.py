# 1)

Numeros = []
itera = -15
while itera < 0:
    Numeros.append(itera)
    itera += 1
print(Numeros)

# 3)

pares = [i for i in Numeros if int(i/2) == float(i/2)]
print(pares)

# 4)

for i in range(3):
    print(pares[i])

# 5)

for i, p in enumerate(pares):
    print(i, p)

# 6)

lista = [1,2,5,7,8,10,13,14,15,17,20]
itera = 0
while itera < len(lista):
    if itera + 1 not in lista:
        lista.insert(itera, itera + 1)
    itera += 1
print(lista)   

# 7)

fibonacci = [0,1]
for i in range(2,30):
    numero = fibonacci[i-1] + fibonacci[i-2]
    fibonacci.append(numero)
print(fibonacci)

# 8)
print(sum(fibonacci))

# 9)
for i in range(24,29):
    print(fibonacci[i+1]/fibonacci[i])

# 10)

cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'
lista = list(cadena)
print(cadena.count("n"))

# 11)

diccionario = {"nombres": ["juan","pablo"], "apellidos": ["perungo", "preucez"]}
for i in diccionario:
    print(i)

# 12)

lista1 = list(cadena)
for i in lista1:
    print(i)

# 13)

a = ["pablo","martin","sebastian"]
b = ["piatti", "palermo", "villa"]
c = zip(a,b)
d = list(c)
print(d)

# 14)

lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]
lis7 = []
for i in lis:
    if int(i/7) == float(i/7):
        lis7.append(i)
    else:
        continue
print(lis7)
