'''Crea una función lambda que filtre los números impares de una lista dada.'''


def es_impar(numero):
    return numero % 2 != 0

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

impares = list(filter(es_impar, numeros))

print(impares)
