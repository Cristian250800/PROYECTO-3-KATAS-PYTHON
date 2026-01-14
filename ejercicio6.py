'''Escribe una función que calcule el factorial de un número de manera recursiva.'''

numero = 5

def calcular_factorial(numero):

    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * calcular_factorial(numero - 1)

print(f"El factorial de {numero} es: {calcular_factorial(numero)}")