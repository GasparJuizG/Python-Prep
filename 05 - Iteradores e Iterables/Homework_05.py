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
    