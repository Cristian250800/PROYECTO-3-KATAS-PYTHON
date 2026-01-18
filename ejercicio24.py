'''Calcula la diferencia total en los valores de una lista. Usa la función reduce().'''

from functools import reduce
numeros = [12,3,446,10]

resultado = reduce(lambda acc, x: acc - x, numeros)

print(f"La diferencia es: {resultado}")
