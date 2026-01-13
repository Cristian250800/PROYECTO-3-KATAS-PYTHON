'''Escribe una función que tome una lista de números como parámetro
y un valor opcional nota_aprobado (por defecto 5). La función debe calcular
 la media de los números en la lista y determinar si la media es mayor
 o igual que nota_aprobado. Si es así, el estado será "aprobado";
de lo contrario, "suspenso". La función debe devolver una tupla que contenga la media y el estado.'''

numeros = [1, 3, 10]

def evaluar_notas(lista, nota_aprobado = 5):

    media = sum(lista) / len(lista)

    if media >= nota_aprobado:
        estado = "aprobado"
    else:
        estado = "suspenso"

    return (media, estado)


print(f"El resultado final es: {evaluar_notas(numeros)}")
