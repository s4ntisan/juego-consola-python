# Esta relacionada con perro.py y es lo mismo que 1.PracticaPOO.py pero haciendo módulos
# Crear instancias de la clase perro

from PracticaPOO.perro import Perro

perro1 = Perro("Firulais", 3) # Apretando control espacio sobre perro me debería traer la clase. De esta manera se crea from PracticaPOO.perro import Perro
perro2 = Perro("luna", 5)

# usamos la instancia.
# usamos template strings con las variables propias de la instancia de una clase (objeto)

print(f"{perro1.nombre} tiene {perro1.edad} años y dice {perro1.ladrar()}")
print(f"{perro2.nombre} tiene {perro2.edad} años y dice {perro2.ladrar()}")