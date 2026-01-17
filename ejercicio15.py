'''Crea una función lambda que sume 3 a cada número de una lista dada.'''

def sumar_tres(n):
    return n + 3

numeros = [1,2,3,4]

resultado = list(map(sumar_tres, numeros))

print(resultado)
