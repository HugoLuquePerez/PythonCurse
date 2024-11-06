# Usar el método list() con una tupla para crear una lista
elementos = ("Hugo", "Luque", 1.85, True)
lista = list(elementos)

# Agrega un elemento a la lista
lista.append("Perez")
print(lista)

# Agrega un elemento a la lista en indice indicado
lista.insert(0,"Piña")
print(lista)

#Agrega varios elementos a la lista
lista.extend(["arroz", "frijoles", "carne"])
print(lista)

#elimina un elemento pide indice y devuelve valor
lista.pop(7)
print(lista)

#Elimina el elmento por su valor
lista.remove("carne")
print(lista)

#Ordenar la lista
lista2 = ["R6","alcachofa","tabaco","morge","baloncesto","MMA"]
lista2.sort()
print(lista2)

#invierte los elementos de la lista
lista.reverse()
print(lista)

#limpiar lista
lista.clear()
print(lista)