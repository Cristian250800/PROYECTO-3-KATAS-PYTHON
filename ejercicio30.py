'''Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.'''


def son_anagramas(palabra1, palabra2):
    return sorted(palabra1.lower()) == sorted(palabra2.lower())


print(f"Estas palabras son anagramas?  { son_anagramas("roma", "amor")}")
