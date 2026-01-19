'''Crea una función que solicite al usuario ingresar una lista de nombres y
luego un nombre para buscar en esa lista. Si el nombre está en la lista,
imprime un mensaje indicando que fue encontrado; de lo contrario, lanza una excepción.
'''

def buscar_nombre():
    nombres = ["ana", "cristian", "maría", "pedro", "sofía"]

    nombre_buscar = input("Introduce el nombre a buscar:\n").lower()

    if nombre_buscar in nombres:
        print(f"El nombre {nombre_buscar} fue encontrado.")
    else:
        raise ValueError(f"El nombre {nombre_buscar} no está en la lista.")

try:
    buscar_nombre()
except ValueError as e:
    print(e)


