nombre = "Juan"
edad = 25

# Usando f-string para insertar variables en la cadena
saludo = f"Hola, mi nombre es {nombre} y tengo {edad} años."
print(saludo)

#Dentro de las llaves {}, se pueden colocar variables o incluso expresiones, como nombre y edad.
#Puedes colocar cualquier tipo de expresión dentro de las llaves, no solo variables. Esto incluye operaciones matemáticas, llamadas a funciones, etc.

a = 10
b = 5

resultado = f"La suma de {a} y {b} es {a + b}."
print(resultado)

#Las f-strings también permiten darle formato a los valores dentro de las llaves. Por ejemplo, puedes formatear números decimales o valores de fecha.

pi = 3.14159265359

# Formatear el número a dos decimales
resultado = f"El valor de pi es aproximadamente {pi:.2f}"
print(resultado)

#El :.2f dentro de las llaves indica que se quiere mostrar el número con 2 decimales. Aquí, .2f es una especificación de formato que se puede usar con números flotantes.

#También puedes usar f-strings con diccionarios y listas, accediendo a sus valores directamente dentro de las llaves.

persona = {"nombre": "Ana", "edad": 30}

mensaje = f"Hola, me llamo {persona['nombre']} y tengo {persona['edad']} años."
print(mensaje)

colores = ["rojo", "verde", "azul"]

mensaje = f"Los colores son: {colores[0]}, {colores[1]}, {colores[2]}"
print(mensaje)

#También puedes realizar llamadas a funciones dentro de las llaves para que el resultado se inserte en la cadena.

def obtener_saludo(nombre):
    return f"¡Hola, {nombre}!"

nombre = "Carlos"
mensaje = f"{obtener_saludo(nombre)} ¿Cómo estás?"
print(mensaje)

#Se llama a la función obtener_saludo dentro de la f-string, y el valor retornado por la función es insertado en la cadena.