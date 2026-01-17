'''Crea una función que retorne las palabras de una lista que comiencen con una letra en específico.
Usa la función filter().'''


def palabras_que_empiezan_con(palabras, letra):
    return list(filter(lambda p: p.startswith(letra), palabras))

lista = ["perro", "gato", "pájaro", "pez", "conejo"]
print(palabras_que_empiezan_con(lista, "c"))

