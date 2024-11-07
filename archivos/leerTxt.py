""" Leer archivos txt y ñadir encoding para no tener problemas de caracteres """

archivoSinleer = open("archivos\\textHugo.txt",encoding="UTF-8")
#leer archivo completo
archivo = archivoSinleer.read() 
#leer linea por linea
""" lineas = archivoSinleer.readlines() """
#leer una sola linea
linea = archivoSinleer.readline()
print(linea)

""" cerrar archivos para poder seguir trabajdno con ellos mas adelante """
archivo.close()