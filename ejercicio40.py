'''Escribe un programa en Python que utilice condicionales para determinar el monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe:
    a. Solicitar al usuario el precio original de un artículo.
    b. Preguntar si tiene un cupón de descuento (respuesta sí o no).
    c. Si la respuesta es sí, solicitar el valor del cupón de descuento.
    d. Aplicar el descuento al precio original, siempre que el valor del cupón sea válido (mayor a cero).
    e. Mostrar el precio final de la compra, considerando o no el descuento.
    f. Usar estructuras de control de flujo (if, elif, else) para llevar a cabo las acciones.'''




def calcular_precio_final():
    try:
        precio = float(input("Introduce el precio del artículo: "))

        if precio <= 0:
            print("La cantidad debe ser mayor que cero")
            return

        tiene_cupon = input("Tienes cupón de descuento? (si/no): ").lower()

        if tiene_cupon == "si":
            descuento = float(input("Introduce el valor del cupón: "))
            precio_final = aplicar_descuento(precio, descuento)
            print(f"Precio final: {precio_final:.2f} €")

        elif tiene_cupon == "no":
            print(f"El precio final del artículo es: {precio} €")

        else:
            print("Datos no válidos")

    except ValueError:
        print("Datos no válidos")

def aplicar_descuento(precio, descuento):
    if descuento > 0 and descuento < precio:
        return precio - descuento
    else:
        return precio


calcular_precio_final()
