'''Crea una función que tome un nombre completo y una lista de empleados, busque el nombre en la lista
 y devuelva el puesto del empleado si se encuentra; de lo contrario,
 devuelve un mensaje indicando que la persona no trabaja aquí.
'''

empleados = [
    {"nombre": "Ana Lopez", "puesto": "Administración"},
    {"nombre": "Carlos Perez", "puesto": "Ventas"},
    {"nombre": "Maria Gomez", "puesto": "Recursos Humanos"},
    {"nombre": "Cristian Mancha", "puesto": "Informática"}
]

def buscar_empleado(nombre_completo):
    for empleado in empleados:
        if empleado["nombre"].lower() == nombre_completo.lower():
            return f"{empleado['nombre']} trabaja en {empleado['puesto']}."
    return "Esa persona no trabaja aquí"

nombre_buscar = input("Introduce el nombre de la persona a buscar: \n")
print(buscar_empleado(nombre_buscar))

