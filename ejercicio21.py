'''Crea una función que calcule el cubo de un número dado mediante una función lambda.'''

def calcular_numero_cubo(numero):
    calcular = lambda x : x ** 3
    return calcular(numero)

numero= int(input("Introduce un número para calcular su cubo: "))
print(calcular_numero_cubo(numero))