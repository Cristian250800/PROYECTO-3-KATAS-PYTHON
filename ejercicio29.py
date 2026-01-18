'''Crea una función que convierta una variable en una cadena de texto
 y enmascare todos los caracteres con el carácter '#' excepto los últimos cuatro.'''

def enmascarar_texto(valor):
    texto = str(valor)
    if len(texto) <= 4:
        return texto
    return '#' * (len(texto) - 4) + texto[-4:]

texto_random = "jdfkajgjka"
print(enmascarar_texto(texto_random))


