import random
from PracticaFinal.enemigo import Enemigo
from PracticaFinal.jugador import Jugador


def main():
    nombre_jugador = input(
        "Bienvenido a la aventura en el Espacio! Por favor, ingresa tu nombre: "
    )
    jugador = Jugador(nombre_jugador)

    enemigos = [ 
        Enemigo("Alien", 50, 10),
        Enemigo("Robot", 30, 5),
        Enemigo("Monstruo", 70, 15),
    ] #Alt + shift + f acomoda el código

    enemigos_derrotados = []

    print("Comienza la aventura")

    # Para hacer que se mantenga en un bucle hasta que ganemos o perdamos

    while enemigos: # Mientras haya enemigos
        enemigo_actual = random.choice(enemigos) #Agarra uno de los 3 enemigos y lo pone como enemigo actual
        if enemigo_actual in enemigos_derrotados: # Para que no se repita un enemigo derrotado
            continue #Saltea el While

        print(f"Te encuentras con un {enemigo_actual.nombre} en tu camino")

        while enemigo_actual.salud > 0: #Vamos a hacer la pelea
            accion = input("¿Que deseas hacer? (atacar/huir): ").lower()

            if accion == "atacar":
                dano_jugador = jugador.atacar()
                print(f"Has causado {dano_jugador} de daño")
                enemigo_actual.recibir_dano(dano_jugador)

                if enemigo_actual.salud > 0:
                    dano_enemigo = enemigo_actual.atacar()
                    print(f"El {enemigo_actual.nombre} te atacó y te causó {dano_enemigo} de daño")
                    jugador.recibir_dano(dano_enemigo)

            elif accion == "huir":
                print("Has decidido huir del combate")
                break # Sale de la estructura actual (While)

        if jugador.salud <= 0:
            print("Has perdido la partida")
            break

        if enemigo_actual.salud <= 0:
            enemigos_derrotados.append(enemigo_actual) # Para no tener en cuenta los enemigos una vez son derrotados
            enemigos.remove(enemigo_actual)

        jugador.ganar_experiencia(20)

        continuar = input("¿Quieres seguir explorando? (s/n) ").lower()

        if continuar != "s":
            print("¡Gracias por haber jugado Batallas Galácticas!")
            break

    if not enemigos: # Si enemigos estuviera vacío
        print("Felicidades has derrotado a todos los enemigos")

if __name__ == "__main__": # nos asegura que solo podremos ejecutar este script desde el programa principal
    main()