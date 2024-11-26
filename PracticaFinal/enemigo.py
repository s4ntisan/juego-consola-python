import random


class Enemigo:
    def __init__(self,nombre,salud,dano):
        self.nombre = nombre
        self.salud = salud
        self.dano = dano

    def atacar(self):
        return random.randint(5,15)
    
    def recibir_dano(self, dano):
        self.salud -= dano
        print(f"Al {self.nombre} le quedan {self.salud} puntos de vida")
        if self.salud <= 0:
            print(f"Has derrotado a {self.nombre}")
            return True # Para terminar el juego
        return False

        
