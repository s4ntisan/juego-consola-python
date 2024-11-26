# Clase base o padre
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        print("El animal hace un sonido")

# Clase derivada o hija
class Gato(Animal):
    def __init__(self, nombre, color):
        super().__init__(nombre)  # Llamamos al constructor de la clase padre
        self.color = color

    # Sobrescribimos el método hacer_sonido
    def hacer_sonido(self):
        print(f"{self.nombre} dice: Miau")

# Crear un objeto de la clase Gato
mi_gato = Gato("Mishi", "Negro")
print(mi_gato.nombre)  # Salida: Mishi
print(mi_gato.color)   # Salida: Negro
mi_gato.hacer_sonido() # Salida: Mishi dice: Miau

# El polimorfismo te permite utilizar el mismo método, pero con comportamientos diferentes según el tipo de objeto que lo ejecute.
# El polimorfismo te permite utilizar un mismo nombre de método (hacer_sonido), pero cada clase lo implementa de una manera específica.
# Sobreescribe el método de la superclase en cada clase y tener su comportamiento definido.

# Usamos las clases anteriores: Animal y Gato
class Perro(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre} dice: Guau")

# Creamos una lista de animales
animales = [Gato("Mishi", "Negro"), Perro("Firulais")]

# Usamos el mismo método para todos, pero cada uno hace un sonido diferente
for animal in animales:
    animal.hacer_sonido()