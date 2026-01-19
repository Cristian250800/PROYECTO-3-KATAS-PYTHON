'''Crea una función lambda que sume elementos correspondientes de dos listas dadas.
'''

lista1 = [1,2,3,4]
lista2 = [1,2,3,4]

def sumar_elementos(a, b):
    return a + b


resultado = list(map(sumar_elementos, lista1, lista2))

print(f"La suma de las listas es {resultado}")


