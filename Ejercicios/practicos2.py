# ejercicio a) 

frase = input('Decime una frase y te calculo cuanto tiempo tardarías en decirla: ')
palabrasSeparadas = frase.split(" ")
cantidadDePalabras = len(palabrasSeparadas)
print(f'Dijistes {cantidadDePalabras} palabras, y tardarías {cantidadDePalabras/2} segundos en decirlo')
print(f'Dalto lo diría en  {cantidadDePalabras * 100 // 2 * 1.3 / 100} segundos.')

if cantidadDePalabras > 120:
    print("Para flaco tampoco te pedí un testamento.")