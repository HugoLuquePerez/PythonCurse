#creando una funcion simple
""" def saludar():
    print("Hola Hugo, que tal maestro ¿Como andas?")

saludar() """

#crear una funcion que tengas parametros

def saludar(nombre):
    print(f"Hola {nombre} mi maestro ¿Como andas?")

""" saludar(input("Hola dime ¿Cual es tu nombre? ")) """

#crear una funcion q rentorne valores 
""" def crearContraseña(num):
    chars = "abcdefghij"
    numEntero = str(num)
    num = int(numEntero[0])
    c1 = numEntero - 2
    c2 = numEntero
    c3 = numEntero - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{numEntero*2}"
    num * 2
    print(contraseña)
    return contraseña

crearContraseña(98) """