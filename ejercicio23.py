'''Concatena una lista de palabras. Usa la función reduce().'''

from functools import reduce

palabras = ["Bebe", "mucha", "agua"]

concatenar_palabras =  reduce(lambda acc, x : acc + " " + x, palabras)

print(concatenar_palabras)