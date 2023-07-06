# Laberint
import os
import random
import readchar

POS_X = 0
POS_Y = 1

obstacle_definition = """\
            ########
#####      ###     #
#####               
#####      #########
           #########
########      ######
########      ######
#####     #####    #
                    
###         ########\
"""

my_position = [1, 0]
map_objects = [[15,1], [4,4],[16,7]]

end_game = False
died = False

#POKEMON VARIABLES
vida_inicial_pikachu = 90
vida_inicial_charmander = 90

vida_pikachu = vida_inicial_pikachu
vida_charmander = vida_inicial_charmander

tamanio_barra_vida = 20

#Ataques pikachu
impactrueno = 12
latigo = 11
at_rapido = 9


# Create obstacle map
obstacle_definition = [list(row) for row in obstacle_definition.split("\n")]

MAP_WIDTH = len(obstacle_definition[0])
MAP_HEIGHT = len(obstacle_definition)

# Main loop
while not end_game:

    # Draw map
    print("+" + "-" * MAP_WIDTH * 2 + "+")

    for cordinate_y in range(MAP_HEIGHT):
        print("|", end="")

        for cordinate_x in range(MAP_WIDTH):

            char_to_draw = "  "
            object_in_cell = None

            for map_object in map_objects:
                if map_object[POS_X] == cordinate_x and map_object[POS_Y] == cordinate_y:
                    char_to_draw = " *"
                    object_in_cell = map_object

            if my_position[POS_X] == cordinate_x and my_position[POS_Y] == cordinate_y:
                char_to_draw = " @"

                if object_in_cell:
                    os.system("cls")
                    map_objects.remove(object_in_cell)
                    print("Te has encontrado con un entrenador pokemon")
                    print("BATALLA POKEMON")

                    while vida_charmander > 0 and vida_pikachu > 0:
                        # Se desenvuelven los turnos de combate
                        #TURNO CHARMANDER
                        print("Turno de Charmander")
                        ataque_charmander = random.randint(1, 2)
                        if ataque_charmander == 1:
                            print("Charmander ataca con arañazo, hace 9 de daño")
                            vida_pikachu -= 9
                        else:
                            print("Charmander ataca con Lanzallamas, hace 11 de daño")
                            vida_pikachu -= 11

                        if vida_pikachu < 0:
                            vida_pikachu = 0
                        if vida_charmander < 0:
                            vida_charmander = 0

                        barra_vida_pikachu = int(vida_pikachu * tamanio_barra_vida / vida_inicial_pikachu)
                        print("Pikachu:    [{}{}] ({} / {})".format("*" * barra_vida_pikachu,
                                                                    " " * (tamanio_barra_vida - barra_vida_pikachu),
                                                                    vida_pikachu, vida_inicial_pikachu))

                        barra_vida_charmander = int(vida_charmander * tamanio_barra_vida / vida_inicial_charmander)
                        print("Charmander:   [{}{}] ({} / {})".format("*" * barra_vida_charmander,
                                                                    " " * (tamanio_barra_vida - barra_vida_charmander),
                                                                    vida_charmander, vida_inicial_charmander))

                        input("Enter para continuar... \n \n")
                        os.system("cls")
                        #TURNO PIKACHU
                        print("Turno Pikachu")

                        ataque_pikachu = None
                        while ataque_pikachu not in ["I", "L", "A"]:
                            ataque_pikachu = input("Que ataque deseas realizar? [I]mpactrueno, [L]atigo, [A]taque rapido")

                        if ataque_pikachu == "I":
                            vida_charmander -= impactrueno
                            print("Pikachu ataca con impactrueno, hace 12 de daño")
                        elif ataque_pikachu == "L":
                            vida_charmander -= latigo
                            print("Pikachu ataca con latigo, hace 11 de daño")
                        elif ataque_pikachu == "A":
                            vida_charmander -= at_rapido
                            print("Pikachu realiza un ataque rapido, hace 9 de daño")

                        if vida_pikachu < 0:
                            vida_pikachu = 0
                        if vida_charmander < 0:
                            vida_charmander = 0

                        barra_vida_pikachu = int(vida_pikachu * tamanio_barra_vida / vida_inicial_pikachu)
                        print("Pikachu:    [{}{}] ({} / {})".format("*" * barra_vida_pikachu,
                                                                    " " * (tamanio_barra_vida - barra_vida_pikachu),
                                                                    vida_pikachu, vida_inicial_pikachu))

                        barra_vida_charmander = int(vida_charmander * tamanio_barra_vida / vida_inicial_charmander)
                        print("Charmander:  [{}{}] ({} / {})".format("*" * barra_vida_charmander, " " *
                                                                     (tamanio_barra_vida - barra_vida_charmander),
                                                                     vida_charmander, vida_inicial_charmander))

                        input("Enter para continuar... \n \n")
                        os.system("cls")

                    if vida_pikachu > vida_charmander:
                        print("Pikachu gana")
                    else:
                        print("Charmander gana")
                        died = True

                    input("Enter para continuar... \n \n")

            vida_pikachu = 90
            vida_charmander = 90

            if obstacle_definition[cordinate_y][cordinate_x] == "#":
                char_to_draw = "##"

            print("{}".format(char_to_draw), end="")
        print("|")

    print("+" + "-" * MAP_WIDTH * 2 + "+")

    # Ask user where he wants to move
    # direction = input("Donde te quieres mover? [WASD]: ")
    direction = readchar.readchar()
    new_position = None

    if direction == "w":
        new_position = [my_position[POS_X], (my_position[POS_Y] - 1) % MAP_HEIGHT]

    elif direction == "s":
        new_position = [my_position[POS_X], (my_position[POS_Y] + 1) % MAP_HEIGHT]

    elif direction == "a":
        new_position = [(my_position[POS_X] - 1) % MAP_WIDTH, my_position[POS_Y]]

    elif direction == "d":
        new_position = [(my_position[POS_X] + 1) % MAP_WIDTH, my_position[POS_Y]]

    elif direction == "q":
        end_game = True

    if new_position:
        if obstacle_definition[new_position[POS_Y]][new_position[POS_X]] != "#":
            my_position = new_position

    os.system("cls")

if died:
    print("HAS PERDIDO!")