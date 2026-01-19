'''Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo", "circulo" o "triangulo")
y datos (una tupla con los datos necesarios para calcular el área de la figura).'''

import math

def calcular_area(figura, datos):
    if figura == "rectangulo":
        base, altura = datos
        return base * altura

    elif figura == "circulo":
        radio, = datos
        return math.pi * radio ** 2

    elif figura == "triangulo":
        base, altura = datos
        return (base * altura) / 2

    else:
        return "Figura no válida"


print(f"El área es del rectangulo es : {calcular_area('rectangulo', (5, 3))}")
print(f"El área es del círculo es : {calcular_area('circulo', (5,))}")
print(f"El área es del triangulo es : {calcular_area('triangulo', (3, 5))}")

