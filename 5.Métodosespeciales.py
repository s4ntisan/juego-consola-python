from MetodosEspeciales.mago import Mago

merlin = Mago ("Merlín", ["Bola de fuego", "Rayo"])
gandalf = Mago ("Gandalf", ["Llamar a las aguilas cuando termino la pelicula", "Bola de fuego"])

print(merlin) #devuelve el método __str__ que habíamos generado
print(len(merlin)) #devuelve el método __len__ que habíamos generado

print(gandalf) #devuelve el método __str__ que habíamos generado
print(len(gandalf)) #devuelve el método __len__ que habíamos generado
print(merlin == gandalf) #devuelve una comparación usando los criterios que definimos en método __eq__

copia_merlin = Mago ("Merlín", ["Bola de fuego", "Rayo"])

print(merlin == copia_merlin) #devuelve una comparación usando los criterios que definimos en método __eq__

mago_combinado = merlin + gandalf #devuelve el método __add__
print(mago_combinado)


