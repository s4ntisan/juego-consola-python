#Imagina que tenemos una clase Animal y luego queremos crear una clase Gato, que herede de Animal pero también tenga su propio comportamiento.

# Clase base o padre o superclase
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        print("El animal hace un sonido")

# Clase derivada o hija o subclase
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

"""La clase Gato hereda de Animal, por lo que tiene acceso al atributo nombre y al método hacer_sonido de Animal.
En el constructor de Gato, usamos super().__init__(nombre) para llamar al constructor de la clase base (Animal) y evitar duplicar el código.
Además, hemos sobrescrito el método hacer_sonido en la clase Gato para que cada tipo de animal haga su propio sonido."""