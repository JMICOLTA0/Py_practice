# added feature to break the roll_dice() once MAX_SCORE is reached

from random import randint
MIN = 1
MAX = 6
MAX_SCORE = 50

def roll_dice():
    return randint(MIN, MAX)

rolled = 0

while True:
    num_players = input('Ingresa numero de jugadores (2-4): ')
    if num_players.isdigit():
        num_players = int(num_players)
        if 2 <= num_players  <= 4:
            break
        else:
            print('Deben ser entre 2 y 4 jugadores')
    else:
        print('Debes ingresar un numero.')

puntaje_jugadores = [0] * num_players # it's the same as: puntaje_jugadores = [0 for _ in range(num_players)]

game_over = False
while not game_over:
    for pl_num in range(num_players):
        print(f'Turno jugador numero {pl_num + 1} ha empezado \nTu puntaje total es: {puntaje_jugadores[pl_num]}')
        total_score = 0

        while True:
            choice = input('Deseas tirar el dado? (y) ').strip().lower()
            if choice == 'y':
                rolled = roll_dice()
                if rolled == 1:
                    print(f'Sacaste un 1! Turno terminado :(')
                    total_score = 0
                    break
                else:
                    total_score += rolled
                    print(f'Sacaste un {rolled}')
                    print(f'El acumulado de este turno es: {total_score}\n')
                    if puntaje_jugadores[pl_num] + total_score >= MAX_SCORE:
                        break
            elif choice == 'n':
                break
            else:
                print(f'Ingresa "y" si deseas volver a lanzar, de lo contrario, ingresa "n".')

        if rolled == 1:
            puntaje_jugadores[pl_num] = 0
        puntaje_jugadores[pl_num] += total_score
        print(f'Tu puntaje total es: {puntaje_jugadores[pl_num]}\n')
        if puntaje_jugadores[pl_num] >= MAX_SCORE:
            game_over = True
higher_score = max(puntaje_jugadores)
winner_index = puntaje_jugadores.index(higher_score)
print(f'Felicidades jugador {winner_index + 1}. Ganaste con un puntaje de {higher_score}!')