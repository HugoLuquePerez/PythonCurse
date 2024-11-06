def calcQualityPlayer(kd):
    kd = float(kd)
    if kd <= 0.10: 
        return 'Conecta el teclado puto manco... Tu rango debería de ser Cobre'
    elif kd <= 0.50:
        return 'Ya es hora de usar esas manos... Tu rango debería de ser Bronce'
    elif kd <= 1:
        return 'Se puede decir que ya eres jugador de R6... Tu rango debería ser Plata'
    elif kd <= 1.2:
        return 'Ya has entrao a la liga de autistas cuidado... Tu rango debería ser Oro'
    elif kd <= 1.5:
        return 'Buen aim pero sigue practicando ijueputa... Tu rango debería ser Platino'
    elif kd <= 1.8:
        return 'Empiezas a ser bueno... Tu rango debería ser Diamante'
    elif kd <= 2:
        return 'Te estas volvieldo un poco psicopata... Tu rango debería ser Esmeralda'
    elif kd <= 2.5:
        return 'Ahora si eres totalmente un psicopata... Tu rango debería ser Champion'
    else:
        return 'Eres un dios absoluto... ¡Tu rango debería ser Gran Maestro!'

askKD = input("Para verificar qué tipo de jugador eres, dime cuál es tu K/D: ")
print(calcQualityPlayer(askKD))
