#Utilizando parametros para una función

def suma(*numeros):
    return sum(numeros)

resultado = suma(4,5,6,7,9)
print(resultado)