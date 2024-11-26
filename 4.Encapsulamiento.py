# Encapsulamiento: Concepto de ocultar los detalles internos de una clase y restringir el acceso a atributos y métodos de la misma
# Para poder utlizar atributos y métodos los debemos tener públicos.

from Encapsulamiento.cuenta_bancaria import CuentaBancaria

#Creamos instancia
cuenta = CuentaBancaria("Sergie Code", 1000)

# Intentar acceder a datos privados:

# print(cuenta.__saldo) Da error porque esta privado
# print(cuenta.__titular) Da error porque esta privado

# Intentar modificar el saldo y el titular de forma directa

cuenta.__titular = "Ricardito"
cuenta.__saldo = 1000000000000000000000

print(cuenta.obtener_saldo()) # aunque haya querido sobreescribir el saldo, no se pudo.

cuenta.depositar(500)
print(cuenta.obtener_saldo())

cuenta.retirar(1000)
print(cuenta.obtener_saldo())

# Intentamos hacer cosas que esten mal

cuenta.depositar(-500)
print(cuenta.obtener_saldo())

cuenta.retirar(8000)
print(cuenta.obtener_saldo())