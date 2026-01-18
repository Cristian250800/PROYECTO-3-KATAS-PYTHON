'''Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.'''

def primer_duplicado (lista):
    elementos = set()
    for elemento in lista:
        if elemento in elementos:
            return elemento
        elementos.add(elemento)


numeros = [3, 5, 1, 2, 5, 7, 3]
resultado = primer_duplicado(numeros)

if resultado:
    print(f"El primer duplicado es: {resultado}")
else:
    print("No hay duplicados")