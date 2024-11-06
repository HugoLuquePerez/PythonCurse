frutas = {"banana","manzana","ciruela","pera","naranja","granada","durazno"}
cadena = "Hola Hugo"
numeros = [2,5,8,10]

#evitando una fruta con la sentencia continue
for fruta in frutas:
    if fruta == 'granada':
        continue
    print(f"Me voy a comer una {fruta}")

#evitar q un bucle siga ejecutandose

for fruta in frutas:
    if fruta == 'granada':
        break
    print(f"Me voy a comer una {fruta}")

#recoriendo una cadena de texto

for letra in cadena:
    print(letra)

#for en una sola inea de codigo

numeroDuplicados = list()
for numero in numeros:
    numeroDuplicados.append()
    print(numeroDuplicados)