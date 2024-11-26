# Definimos la clase Perro
class Perro:
    # El constructor (__init__) es un método especial para inicializar los atributos del objeto
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo nombre
        self.edad = edad      # Atributo edad

    # Un método que hace que el perro "ladré"
    def ladrar(self):
        print(f"{self.nombre} está ladrando: ¡Guau, guau!")

# Crear un objeto de la clase Perro
mi_perro = Perro("Firulais", 3)

# Acceder a los atributos y métodos
print(mi_perro.nombre)  # Salida: Firulais
print(mi_perro.edad)    # Salida: 3
mi_perro.ladrar()       # Salida: Firulais está ladrando: ¡Guau, guau!