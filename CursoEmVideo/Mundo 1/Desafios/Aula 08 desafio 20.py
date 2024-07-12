from random import shuffle

print('Escreva o nome dos participantes.')
N1 = str(input('Do primeiro: '))
N2 = str(input('Do segundo: '))
N3 = str(input('Do terceiro: '))
N4 = str(input('Do quarto: '))

Sorteio = [N1, N2, N3, N4]
shuffle(Sorteio)

print(f'a ordem de apresentação será {Sorteio}')

