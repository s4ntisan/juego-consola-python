from Herencia.personaje import Personaje

class Heroe(Personaje): #hereda los atributos de personaje
    def __init__(self, nombre, salud ,poder): # nombre y salud es obligatorio (ya estaba en personaje)
        super().__init__(nombre,salud)  #con super() lo asigno a la clase de la cual heredo. Es propio de personaje
        # en otras palabras, esto me permite asignar los valores a los atributos heredados. Con super llamo a la instancia personaje y con init llamo al constructor de personaje
        self.poder = poder # poder al ser nuevo, lo tengo que asignar a la nueva clase
        
    def mostrar_poder(self):
        print(f"{self.nombre} tiene el poder de {self.poder}")