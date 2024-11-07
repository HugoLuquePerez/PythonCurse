#escribir en un archivo txt desde uno py

with open("archivos\\textHugo.txt","w",encoding="UTF-8") as archivo:
    # Sobre escribiendo el archivo
    """ archivo.write("JAJjajaJaj te la recontra de pie") """
    # Escribir añadiendo una linea, sobre escribe por primera vez las demas deja una frase tras otra
    archivo.writelines(["Hola maestro como andas\n","Misericordia"])