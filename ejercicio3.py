'''Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros.
La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.'''

def filtrar_palabras(lista, objetivo):
    return [palabra for palabra in lista if objetivo in palabra]


palabras = ["manzana", "banana", "mandragora", "sandía", "mandarina"]

palabra_objetivo = "man"

resultado = filtrar_palabras(palabras, palabra_objetivo)
print(resultado)
