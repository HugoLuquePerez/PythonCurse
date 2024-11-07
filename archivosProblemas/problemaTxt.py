# Dos listas una con nombres y otras con apellidos
nombres = ["Lucas","Matias","Camila","Pedro","roberto"]
apellidos = ["Dalto","Zing","Perez","Luque","Garcia"]
#registrar esta informacion en un TXT de forma optima

with open("nombresApellidos.txt","w")as arch:
    for n,a in zip(nombres,apellidos):
        arch.writelines(f"Nombre {n}\nApellido: {a}\n------------\n")