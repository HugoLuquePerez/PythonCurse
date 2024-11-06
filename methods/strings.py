saludo = "Hello World"
""" print(dir(saludo)) """

""" Convierte mayus """
saludoMayus = saludo.upper()
print(saludoMayus)

""" convierte a minusculas """
saludoMinusculas = saludo.lower()
print(saludoMinusculas)

""" Primera letra Mayusculas """
saludoCapitalize = saludo.capitalize()
print(saludoCapitalize)

""" Encuentra la primera apracion del valor si no devuelve 1 """
findLetter = saludo.find("a")
print(findLetter)
findLetter = saludo.find("e")
print(findLetter)

""" Encuentra la primera aprricion y devuelve la excepcion """
indexLetter = saludo.index("e")
print(indexLetter)

""" verifica si es numerico """
isNumeric = saludo.isnumeric()
print(isNumeric)

""" verifica si es alfanumerico """
isAlpha = saludo.isalpha()
print(isAlpha)

""" Devuelve el numero de veces que se ha encontrado el valor """
countLetter = saludo.count("o")
print(countLetter)

""" Cuenta los caracteres de una cadena """
countChars = len(saludo)
print(countChars)

""" Verifica si termina con X """
endWith = saludo.endswith("ld")
print(endWith)

""" Verifica si empiza con X """
startsWith = saludo.startswith("H")
print(startsWith)

""" Replaza un valor por otro """
replace =  saludo.replace("World", "Land")
print(replace)

""" divide por el parametro dado """
split = saludo.split(" ")
print(split)