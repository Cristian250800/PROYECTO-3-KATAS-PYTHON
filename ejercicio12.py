'''Genera una función que, al recibir una frase, devuelva una lista con la longitud de cada palabra.
Usa la función map().'''


def longitud_palabras(frase):
    return list(map(len, frase.split()))

frase = input("Introduce una frase:\n")
resultado = longitud_palabras(frase)
print(resultado)
