'''Escribe un programa que determine qué calificación en texto tiene un alumno según su calificación numérica.
Reglas:
        0 - 69: insuficiente
        70 - 79: bien
        80 - 89: muy bien
        90 - 100: excelente'''

def sacar_nota(nota):
    if 0 <= nota <= 69:
        return "insuficiente"
    elif 70 <= nota <= 79:
        return "bien"
    elif 80 <= nota <= 89:
        return "muy bien"
    elif 90 <= nota <= 100:
        return "excelente"
    else:
        return "Número no válido"


try:
    nota = int(input("Introduce la calificación (0 a 100): "))
    print("La calificación es:", sacar_nota(nota))
except ValueError:
    print("Debes introducir un número entero")
