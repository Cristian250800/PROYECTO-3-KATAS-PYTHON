'''Escribe un programa que pida al usuario dos números e intente dividirlos.
 Si el usuario ingresa un valor no numérico o intenta dividir por cero,
 maneja esas excepciones de manera adecuada y muestra un mensaje indicando si la división fue exitosa o no.'''


def division(num1, num2):
    try:
        return f"La división es: {num1 / num2}"
    except ZeroDivisionError:
        return "No se puede dividir entre 0"

print("Bienvenido a la calculadora de divisiones")

try:
    numA = int(input("Escribe un número: \n"))
    numB = int(input("Escribe otro número: \n"))
    print(division(numA, numB))
except ValueError:
    print("Entrada inválida, introduce números")
