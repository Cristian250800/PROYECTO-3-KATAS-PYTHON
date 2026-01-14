'''Escribe una función que tome una lista de nombres de mascotas como parámetro
y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España.
La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]. Usa la función filter().'''

mascotas_excluidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
mis_mascotas = ["Mapache", "Cacatúa", "Oso", "Hormiga", "Murciélago"]

def es_mascota_permitida(nombre):

    return nombre not in mascotas_excluidas

resultado_objeto = list(filter(es_mascota_permitida, mis_mascotas))

print(resultado_objeto)