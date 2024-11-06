#Creando una funcion de 3 parametros
def frase(nombre,apellidos,adjetivo):
    return f'Hola {nombre} {apellidos}, sos muy {adjetivo}'

#utilizando keyword arguments
RFrase = frase(nombre="Hugo", apellidos="Luque Pérez", adjetivo="Titán")
print(RFrase)