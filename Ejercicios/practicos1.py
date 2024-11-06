#Promedio de duración
otrosCursosMin = 2.5 
otrosCursosMax = 7
otrosCursosPromedio = 4
daltoCurso = 1.5

#Duracion de crudos

crudoPromedio = 5
crudoDalto = 3.5

#Diferencias de duración

diferenciaConMin = 100 - daltoCurso / otrosCursosMin * 100
diferenciaConMax = 100 - daltoCurso / otrosCursosMax * 100
diferenciaConPromedio = 100 - daltoCurso / otrosCursosPromedio * 100

#porcentaje de crudos

tiempoVacioPromedio = 100 - otrosCursosPromedio * 1000 // crudoPromedio / 10
tiempoVacioDalto = 100 - otrosCursosPromedio * 1000 // crudoDalto / 10

#Mostrar por pantalla la diferencias de duracion

print(f'El curso de Dalto dura un{diferenciaConMin}% menos que el más rapido')
print(f'El curso de Dalto dura un{diferenciaConMax}% menos que el más rapido')
print(f'El curso de Dalto dura un{diferenciaConPromedio}% menos que el más rapido')

#Mostrando el tiempo vacio q se remueve

print(f'Un curso promedio elimina un {tiempoVacioPromedio}% de tiempo vacio')
print(f'Este cursos elimino el {tiempoVacioDalto}% de tiempo vacio')