'''Crea una función llamada procesar_texto
Procesa un texto según la opción especificada: contar_palabras, reemplazar_palabras o eliminar_palabra.
Código a seguir:
Crear una función contar_palabras que cuente el número de veces que aparece cada palabra en el texto y devuelva un diccionario.
Crear una función reemplazar_palabras para sustituir una palabra_original por una palabra_nueva en el texto y devolver el texto modificado.
Crear una función eliminar_palabra que elimine una palabra del texto y devuelva el texto sin ella.
Crear la función procesar_texto que reciba un texto, una opción ("contar", "reemplazar", "eliminar") y un número variable de argumentos según la opción elegida.
'''


def contar_palabras(texto):
    palabras = texto.lower().split()
    conteo = {}

    for palabra in palabras:
        conteo[palabra] = conteo.get(palabra, 0) + 1

    return conteo


def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    return texto.replace(palabra_original, palabra_nueva)


def eliminar_palabra(texto, palabra):
    palabras = texto.split()
    palabras_filtradas = [p for p in palabras if p != palabra]
    return " ".join(palabras_filtradas)


def procesar_texto(texto, opcion, *args):
    if opcion == "contar":
        return contar_palabras(texto)

    elif opcion == "reemplazar":
        return reemplazar_palabras(texto, args[0], args[1])

    elif opcion == "eliminar":
        return eliminar_palabra(texto, args[0])

    else:
        raise ValueError("Opción no válida")


'''Caso de uso:
Verificar el funcionamiento completo de procesar_texto.'''

texto = "Hola mundo!"

print("Contar palabras:")
print(procesar_texto(texto, "contar"))

print("\nReemplazar palabras:")
print(procesar_texto(texto, "reemplazar", "mundo", "Python"))

print("\nEliminar palabra:")
print(procesar_texto(texto, "eliminar", "Hola"))
