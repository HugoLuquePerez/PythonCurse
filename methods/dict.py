dicionario = {
    'nombre' : "Hugo",
    "apellido" : "Luque",
    "edad" : 20
}

""" devuelve las claves """
keys = dicionario.keys()
print(keys)

""" Devuelve el valor """
gets = dicionario.get("nombre")
print(dicionario)

""" pop para eliminar algun valor """
elimnar = dicionario.pop("nombre")
print(dicionario)

""" clear para limpiar el dict """
dicionario.clear()
