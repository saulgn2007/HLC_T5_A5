# Crea una clase CuentaBancaria con un atributo saldo. Implementa métodos para consultar el 
# saldo (ver_saldo()), depositar (depositar(monto)) y retirar (retirar(monto)) con validaciones.

class CuentaBancaria:
    def __init__(self, saldo):
        self.saldo = saldo
        
    def ver_saldo(self):
        print(f"Su saldo es de ${self.saldo}.")
        
    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"Se ha depositado ${monto}.")
        else:
            print("El monto a depositar debe ser mayor a 0.")
        
    def retirar(self, monto):
        if monto > 0:
            if monto <= self.saldo:
                self.saldo -= monto
                print(f"Se ha retirado ${monto}.")
            else:
                print("No se puede retirar más de lo que tiene en su cuenta.")
        else:
            print("El monto a retirar debe ser mayor a 0.")

cuenta = CuentaBancaria(1000)
cuenta.depositar(500)
cuenta.retirar(300)
cuenta.ver_saldo()