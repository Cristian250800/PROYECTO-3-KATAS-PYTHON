'''Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor
no numérico o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120),
 maneja las excepciones adecuadamente.'''

try:
    edad = int(input("Cuál es tu edad?\n"))

    if not 0 <= edad <= 120:
        raise ValueError

except ValueError:
    print("Introduce una edad válida entre 0 y 120")

else:
    print(f"Tu edad es: {edad}")

