# 1)

ListaCiudades = ["Moscu", "Roma", "Berlin", "Tokio", "Lima"]

# 2)

print(ListaCiudades[1])

# 3) 

for i in range(1,4):
    print(ListaCiudades[i])

# 4)

print(type(ListaCiudades))

# 5)

print(ListaCiudades[2:])

# 6)

print(ListaCiudades[:4])

# 7)

ListaCiudades.append("Roma")
ListaCiudades.append("Sucre")


# 8)

ListaCiudades.insert(3, "Dakar")


# 9)

ListaCiudades.extend(["La Paz", "Sidney"])
print(ListaCiudades)

# 10)

print(ListaCiudades.index("Roma"))

# 12)

ListaCiudades.remove("Roma")
print(ListaCiudades)

# 14)

ultimo = ListaCiudades.pop()
print(ultimo)

# 15)
print(ListaCiudades * 4)

# 16)
tupla = []
for i in range(1, 21):
    tupla.append(i)
tupla = tuple(tupla)
print(tupla)

# 17)

print(tupla[10:15])

# 18)

for i in range(20, 31):
    if i not in tupla:
        print(f"{i} no esta en la tupla")
    else:
        print(f"{i} esta en la tupla")

# 19)

if "Paris" in ListaCiudades:
    print("ya esta en la lista")
else:
    ListaCiudades.append("Paris")
    print(ListaCiudades)

# 20)

ciudad = input("ingrese ciudad: ")
print(f"La ciudad aparece {ListaCiudades.count(ciudad)} veces")

# 21)

tupla = list(tupla)
print(tupla)

# 22)
ListaCiudades = tuple(ListaCiudades)
print(ListaCiudades)
ciudad1, ciudad2, ciudad3 = ListaCiudades
print(f"{ciudad1}, {ciudad2}, {ciudad3}")