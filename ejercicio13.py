''' Genera una función que, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra
 en mayúsculas y minúsculas. Las letras no pueden estar repetidas.
 Usa la función map().'''


def convertir_letra(letra):
    return (letra.upper(), letra.lower())

def letras_mayus_minus(conjunto):
    letras_unicas = []
    for c in conjunto:
        if c not in letras_unicas:
            letras_unicas.append(c)
    return list(map(convertir_letra, letras_unicas))

print(letras_mayus_minus("aBc"))
