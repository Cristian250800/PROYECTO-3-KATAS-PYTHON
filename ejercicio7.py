'''Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()'''

lista_tuplas = [("7",), (".",), ("-")]

def convertir(lista):

    return list(map(lambda x: " ".join(x), lista))

print(convertir(lista_tuplas))