class Personaje:
    def __init__(self, nombre, salud):
        self.nombre = nombre
        self.salud = salud

    def identificarse(self):
        print(f"Hola soy {self.nombre}")

    def mostrar_salud(self):
        print(f"{self.nombre} tiene {self.salud} puntos de salud")

# Class personaje va a ser la clase padre o superclase para crear villanos y heroes