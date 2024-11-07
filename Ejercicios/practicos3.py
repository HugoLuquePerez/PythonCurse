#falto el profe y los pibes van armar la clase

#pedir el nombre y la edad a los compañeros que vinieron hoy a clase
def obtenerCompañeros(cantidad):
    compañeros = []
    for i in range(cantidad):
        nombre = input("Ingrese el nombre del compañero: ")
        edad = int(input("Ingrese la edad del compañero: "))
        compañero = (nombre,edad)
        compañeros.append(compañero)
    compañeros.sort(key=lambda x:x[1])
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    return asistente,profesor

asistente,profesor = obtenerCompañeros(3)
print(f"El profesor es: {profesor} y su asistente es: {asistente}")