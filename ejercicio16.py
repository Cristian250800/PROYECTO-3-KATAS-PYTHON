'''Escribe una función que tome una cadena de texto y un número entero n como parámetros
y devuelva una lista de todas las palabras que sean más largas que n.
Usa la función filter().'''

def palabra_mas_largas(cadena, n):
    return list(filter(lambda palabra: len(palabra) > n, cadena.split()))

frase = "Hola me llamo Cristian y estoy programando"
resultado = palabra_mas_largas(frase, 7)
print(resultado)

