# Definiendo la clase (plantilla)
class Perro:
    #Método constructor (__init__)
    def __init__(self, nombre, edad): #self: instancia de perro. Permite tener control de la instancia
        self.nombre = nombre #Al atributo nombre de la instancia le asignamos "nombre" que nos envían como argumento en el constructor
        self.edad = edad #Al atributo edad de la instancia le asignamos "edad" que nos envían como argumento en el constructor

    def ladrar(self): #metodo: comportamiento propio de la clase
        return "Guau"
    
# terminamos de crear la clase

# Vamos a instanciar (llamar) la clase.
# Crear instancias de la clase perro

perro1 =  Perro("Firulais", 3) # Esta llamando por detrás al constructor pasandole nombre y edad
perro2 = Perro("luna", 5)

# usamos la instancia.
# usamos template strings con las variables propias de la instancia de una clase (objeto)


print(f"{perro1.nombre} tiene {perro1.edad} años y dice {perro1.ladrar()}")
print(f"{perro2.nombre} tiene {perro2.edad} años y dice {perro2.ladrar()}")

