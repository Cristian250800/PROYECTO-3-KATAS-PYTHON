'''Crea una función que tome una lista de dígitos y devuelva el número correspondiente.
Por ejemplo, [5,7,2] corresponde al número 572. Usa la función reduce(). '''


from functools import reduce

def convertir_digitos_numeros(digitos):
    return reduce(lambda x, y: x * 10 + y, digitos)

lista = [5, 7, 2]
resultado = convertir_digitos_numeros(lista)
print(resultado)
