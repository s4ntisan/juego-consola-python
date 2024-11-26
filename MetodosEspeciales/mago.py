class Mago:
    #Metodo especial: constructor
    def __init__(self, nombre, hechizos = None): #Hechizos se inicializa como None.
        self.nombre = nombre
        self.hechizos = hechizos if hechizos else [] #Si existen los hechizos pongo los hechizos que me manden, si no pongo una lista vacía.

    #Metodo especial: TO STRING (Se identifica con una cadena de caracteres la instancia)
    def __str__(self): # devolver una cadena de caracteres que defina que es lo que voy a estar devolviendo
        return f"Hola, mi nombre es {self.nombre}, el mago"

    def __len__(self): #para ver que tamaño tiene 
        return len(self.hechizos)
    
    def __eq__(self,otro): #para comparar otro mago (igual nombre e igual hechizo)
        return self.nombre == otro.nombre and self.hechizos == otro.hechizos

    def __add__(self,otro):
        if isinstance(otro,Mago): #tenemos que chequear que sea una isntancia de mago
            return Mago(f"{self.nombre}-{otro.nombre}")
        else:
            raise TypeError("Solo puedes combinar dos magos") # raise: sirve para lanzar un error
        
