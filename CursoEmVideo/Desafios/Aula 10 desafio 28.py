from random import randint
n1 = randint(0, 5)
n2 = int(input('digite um número de 0 a 5: '))

if n1 == n2:
    print(f'PARABÉNS VOCÊ VENCEU O NÚMERO É {n1}')
else:
    print(f'Errado o número é {n1}')

