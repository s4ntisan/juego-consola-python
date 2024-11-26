class CuentaBancaria: 
    def __init__(self,titular,saldo_inicial):
        self.__titular = titular #__ hace privado al atributo (no se puede acceder desde afuera). Solo se puede acceder mediante un método público
        self.__saldo = saldo_inicial #no hace falta que coincidan los nombres saldo = saldo_inicial

    #Setter (editor, configurador) 
    def depositar(self,cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Depósito de ${cantidad} exitoso")
        else:
            print("Error: La cantidad a depositar debe ser mayor a 0")

    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Se ha retirado ${cantidad} exitosamente")
        else:
            print("Fondos insuficientes o cantidad inválida")

    #Getter(obtener información privada a través de un método público)

    def obtener_saldo(self):
        return f"El saldo actual de la cuenta es {self.__saldo}"
    
