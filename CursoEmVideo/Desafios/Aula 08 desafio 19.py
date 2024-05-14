import random

N1 = str(input('digite o nome do 1° aluno: '))
N2 = str(input('digite o nome do 2º aluno: '))
N3 = str(input('digite o nome do 3° aluno: '))
N4 = str(input('digite o nome do 4º aluno: '))

Sorteio = [N1, N2, N3, N4]

ganhador = random.choice(Sorteio)

print(f'o ganhador foi {ganhador}')
