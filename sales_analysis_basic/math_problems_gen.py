import random
import time

OPERATORS = ['+', '-', '*']
MIN_OP = 3
MAX_OP = 12
TOTAL_PROBLEMS = 10

def generate_problem():
    left = str(random.randint(MIN_OP, MAX_OP)) # convertir el valor a string, para poder usarlo en eval function
    right = str(random.randint(MIN_OP, MAX_OP))
    operator = random.choice(OPERATORS)

    expr = left + ' ' + operator + ' ' + right  # también podría convertir left and right en str en este punto
    result = eval(expr)
    return expr, result

wrong = 0
input('Presiona enter para empezar!')
print('---------------------------------')
start_time = time.time()

seen = set()
for i in range(TOTAL_PROBLEMS):
    expr, result = generate_problem()
    while expr in seen:
        expr, result = generate_problem()
    seen.add(expr)
    while True:
        guess = input(f'Problema # {str(i + 1)}: ( {expr} )= ')
        if guess == str(result):
            break
        wrong += 1

end_time = time.time()
total_time = round(end_time - start_time)

print('---------------------------------')
errors = 'No tuviste ningún error!' if wrong == 0 else 'Tuviste solo un error' if wrong == 1 else 'Tuviste ' + str(wrong) + ' errores'
print(f'Buen trabajo, terminaste en {total_time} segundos. {errors}')


