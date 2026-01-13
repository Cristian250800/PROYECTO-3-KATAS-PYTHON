'''Escribe una función que reciba una cadena de texto como parámetro y
devuelva un diccionario con las frecuencias de cada letra en la cadena.
 Los espacios no deben ser considerados.'''

def frecuencias(frase):
    suma_frecuencias = {}

    for letra in frase:
        if letra != " ":
            if letra in suma_frecuencias:
                suma_frecuencias[letra] += 1
            else:
                suma_frecuencias[letra] = 1
    return suma_frecuencias


print(frecuencias("Hola, estoy programando en Python"))