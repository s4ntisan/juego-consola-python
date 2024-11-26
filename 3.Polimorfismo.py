from Polimorfismo.gato import Gato
from Polimorfismo.perro import Perro
from Polimorfismo.vaca import Vaca

#Polimorfismo: Capacidad de los objetos de diferentes clases de responder al mismo método de forma distinta

def hacer_sonido_de_animal(animal):
    print(f"{animal.nombre} hace {animal.hacer_sonido()}")

perro = Perro("Firulais")
gato = Gato("Pelusa")
vaca = Vaca("Lechera")

hacer_sonido_de_animal (perro)
hacer_sonido_de_animal (gato)
hacer_sonido_de_animal (vaca)