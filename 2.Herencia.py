# Herencia: Permite a una clase heredar atributos y metodos de otra clase
# Relacionado con personaje, heroe y villano

from Herencia.heroe import Heroe
from Herencia.villano import Villano

superman = Heroe("Superman", 100, "Volar")
joker = Villano("Joker", 80, "Robar bancos") 

#---------------------------------------------

superman.identificarse() # Viene de la superclase, heredado
superman.mostrar_salud() # Viene de la superclase, heredado
superman.mostrar_poder() # Metodo (comportamiento) propio de heroe

joker.identificarse()
joker.mostrar_salud()
joker.mostrar_habilidad()
