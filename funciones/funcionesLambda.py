""" Para ahorrarnos abrir un bloque de codigo como una funcion para multiplicar podemos usar lambda como parametros """

multiplicarPorDos = lambda x : x*2
print(multiplicarPorDos(5))

""" Creando funcion comun q diga si es par o no """
numeros = [1,2,3,4,5,6,7,8,9]

def esPar(num):
    if (num%2==0):
        return True
numerosPares = filter()
""" usando filter con una funcion común """
