'''Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map(). '''

def duplicar_valores(x):
    return x * 2

numeros = [1, 2, 3, 4, 5]

dobles = list(map(duplicar_valores, numeros))

print(dobles)
