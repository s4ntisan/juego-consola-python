# Esta relacionada con 1.2main y es lo mismo que 1.PracticaPOO.py pero haciendo módulos
# Separo la clase de los objetos

# Definiendo la clase (plantilla)
class Perro:
    #Método constructor (__init__)
    def __init__(self, nombre, edad): #self: instancia de perro. Permite tener control de la instancia
        self.nombre = nombre #Al atributo nombre de la instancia le asignamos "nombre" que nos envían como argumento en el constructor
        self.edad = edad #Al atributo edad de la instancia le asignamos "edad" que nos envían como argumento en el constructor

    def ladrar(self): #metodo: comportamiento propio de la clase
        return "Guau"