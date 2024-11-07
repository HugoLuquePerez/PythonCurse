""" import moduloSaludar """
""" import moduloSaludar as mSaludar """
""" from moduloSaludar import saludar, saludarRaro as saludarCoscu
saludoRaro = saludarCoscu("lucas")
saludo = saludar("Hugo")
print(saludo)
print(saludoRaro) """

""" cuando el modulo esta dentro de una carpeta por delante del directorio actual """
""" from funcionesbuenas.moduloSaludarBuenas import saludarRaro
print(saludarRaro("Hugo")) """

import sys
sys.path.append('C:\\Users\\Hugo\\Desktop\\PythonCurse\\pruebaErutamiento')
