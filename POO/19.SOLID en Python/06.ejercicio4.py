"""
EJERCICIO con el proposito de aplicar la mayor cantidad de conceptos posibles de POO
(Sin descuidar los principios S.O.L.I.D)

>>> CREAR UN JUEGO DE RPG (Jugable desde consola unicamente)

    -> Descripcion: El jugador se sumerge en un mundo medieval lleno de magia, criaturas misteriosas
                    y tesoros ocultos. 
                    El objetivo principal del juego es enfrentarse a enemigos y reunir los 7 tesoros que 
                    contienen pegarminos con poder magico para aumentar las habilidades de los personajes + monedas de oro
    -> Requerimientos:
                    -> Personajes: 
                            - Guerrero, puede atacar con espada y defenderse con escudo (Sin mana)
                            - Mago, Lanza bolas de fuego y crea barreras magicas para defenderse (Con mana)
                            - Paladin, puede atacar con la espada y defenderse con barreras magicas (Mitad de mana que el mago)
                            - Herrero, es el que fabrica las armaduras para los demas personajes (Sin mana) 
                    -> Mecanicas del juego:
                            - Cada personaje tiene una barra de salud (HP) y habilidades unicas
                            - Los tesoros aumentan las stats de los personajes + monedas de oro
                            - Crear un menu con opciones para: Empezar a jugar, elegir clase y nombre de nuestro personaje de cabecera,
                                seleccionar cantidad de enemigos y salir del juego
    -> Criterios de aceptacion:  
                    - Cada personaje debe poder realizar las habilidades especificadas en los requerimientos
                    - Las status comunes a todos los personajes luchadores son ataque, defensa y HP
                    - Los herreros tienen HP y pueden crear espadas, armaduras y escudos
                    - Los tesoros se otorgaran al ganador de cada ronda
                    - La cantidad de rondas sera igual a la cantidad de personajes introducidos (sin contar nuestro personaje)
                    - Cada opcion del menu principal debe realizar lo indicado en la seccion "Mecanicas del juego"
                    - Finalizaicon del juego: El juego finaliza cuando el jugador gana a todos los personajes o pierde una sola vez
                    - Si el juegador pierde, se borraran los datos del mismo
                    - Si el jugador gana, su personaje se mantendra guardado
"""