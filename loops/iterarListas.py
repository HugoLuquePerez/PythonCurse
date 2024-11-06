animales = ["gato","perro","loro","cocodrilo"]
numeros = [52,16,14,72]

#recorriendo animales
for animal in animales:
    print(f'Ahora la variable animal es igual a: {animal}')

#iterando numeros y modificando

for numero in numeros:
    resultado = numero * 10
    print(resultado)

#usando zip para recorrer dos listas a la vez

for numero,animal in zip(animales,numeros):
    print(f"recorriendo lista 1: {numero}")
    print(f"recorriendo lista 2: {animal}")



for num in range(5,10):
    print(num)