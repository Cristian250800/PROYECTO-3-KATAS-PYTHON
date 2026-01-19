'''Genera un programa que nos indique si es de noche, de día o de tarde según la hora proporcionada por el usuario.'''

def momento_del_dia(hora):
    if 6 <= hora < 12:
        return "Es de día"
    elif 12 <= hora < 20:
        return "Es de tarde"
    else:
        return "Es de noche"


try:
    hora = int(input("Introduce una hora (0 a 23): "))

    if hora < 0 or hora > 23:
        print("Hora no válida")
    else:
        print(momento_del_dia(hora))

except ValueError:
    print("Debes introducir un número entero")
