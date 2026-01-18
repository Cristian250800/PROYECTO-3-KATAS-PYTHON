'''Crea una función que calcule el promedio de una lista de números.'''

def calcular_promedio (lista):

    return sum(lista) / len(lista)

numeros = [1,2,3,4,5,6,7]

print("El promedio es: " + str(calcular_promedio(numeros)))