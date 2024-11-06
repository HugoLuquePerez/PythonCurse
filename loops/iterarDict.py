diccionario = {
    "nombre": "Hugo",
    "apellido": "Luque",
    "money": 1000
}

#recorriendo diccionario para obtener solo las claves

for key in diccionario:
    key
    print(f"la clave es: {key}")

#recorriendo un diccionario con items() para obtener la clave y el valor

for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f"la clave es: {key} y el valor es: {value}")

