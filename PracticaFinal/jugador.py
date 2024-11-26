import random

class Jugador:
    def __init__(self,nombre):
        self.nombre = nombre 
        #va a tener atributos que no nos van a pasar y van a empezar con un valor que yo ponga
        self.salud = 100
        self.nivel = 1
        self.experiencia = 0

    def atacar(self):
        return random.randint(10,20) * self.nivel
    
    def recibir_dano(self,dano): #colocamos dano porque no se suelen utilizar eñe (ñ)
        self.salud -= dano
        if (self.salud) <= 0:
            print(f"{self.nombre} ha muerto. Game Over")
        else:
            print(f"Te quedan {self.salud} puntos de salud")

    def ganar_experiencia(self,experiencia):
        print(f"{self.nombre} ha ganado {experiencia} puntos de experiencia" )
        self.experiencia += experiencia
        if self.experiencia >= 100:
            self.nivel +=1
            self.experiencia = 0
            print(f"{self.nombre} ha subido de nivel a {self.nivel}")