'''Escribe una función que reciba una lista de números y calcule su promedio.
 Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.'''

def calcular_promedio(numeros):
    if not numeros:
        raise ValueError("La lista está vacía.")
    return sum(numeros) / len(numeros)

try:
    lista = [1,2,3,4]
    resultado = calcular_promedio(lista)
    print(f"El promedio es: {resultado}")
except ValueError as e:
    print(f"Error: {e}")
