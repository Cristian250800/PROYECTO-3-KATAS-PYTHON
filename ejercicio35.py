'''Crea la clase UsuarioBanco
Representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente.
Métodos: retirar_dinero, transferir_dinero, agregar_dinero.
Código a seguir:
Inicializar un usuario con nombre, saldo y un indicador (True o False) de cuenta corriente.
Implementar retirar_dinero para sustraer dinero del saldo, lanzando un error si no es posible.
Implementar transferir_dinero para transferir dinero desde otro usuario, lanzando un error en caso de fallo.
Implementar agregar_dinero para aumentar el saldo del usuario.
'''

class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, cantidad):
        if cantidad > self.saldo:
            raise ValueError(f"{self.nombre} dispones de saldo insuficiente.")
        self.saldo -= cantidad
        print(f"{self.nombre} ha retirado {cantidad}. Saldo actual: {self.saldo}")

    def transferir_dinero(self, cantidad, otro_usuario):
        if cantidad > self.saldo:
            raise ValueError(f"{self.nombre} no tienes suficiente saldo para transferir {cantidad}.")
        self.saldo -= cantidad
        otro_usuario.saldo += cantidad
        print(f"{self.nombre} ha transferido {cantidad} a {otro_usuario.nombre}. Saldo actual: {self.saldo}")

    def agregar_dinero(self, cantidad):
        self.saldo += cantidad
        print(f"{self.nombre} ha ingresado {cantidad}. Saldo actual: {self.saldo}")


# a. Crear dos usuarios
alicia = UsuarioBanco("Alicia", 100, True)
bob = UsuarioBanco("Bob", 50, True)

# b. Agregar 20 unidades al saldo de Bob
bob.agregar_dinero(20)

# c. Transferir 80 unidades de Bob a Alicia
try:
    bob.transferir_dinero(80, alicia)
except ValueError as e:
    print(e)

# d. Retirar 50 unidades del saldo de Alicia
try:
    alicia.retirar_dinero(50)
except ValueError as e:
    print(e)

# Mostrar saldos finales
print(f"Saldo final de Alicia: {alicia.saldo}")
print(f"Saldo final de Bob: {bob.saldo}")
