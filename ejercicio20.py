'''Para una lista con elementos de tipo integer y string, obtén una nueva lista solo con los valores int.
Usa la función filter().'''


def es_int(elemento):
    return isinstance(elemento, int)

lista = [1, "hola", 3, "mundo", 5, "666", 8]

solo_enteros = list(filter(es_int, lista))

print(solo_enteros)
