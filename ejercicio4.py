'''Genera una función que calcule la diferencia entre los valores de dos listas.
Usa la función map().'''

def restar_listas (a, b):

    return a - b

listaA = [1,2,3,4,5]
listaB = [5,4,3,2,1]

resultado = list(map(restar_listas,listaA,listaB))

print(resultado)