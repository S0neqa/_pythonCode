n = int(input('Digite um número: '))
number = n % 2

if number == 0:
    # Par
    print(f'O número {n} é par.')
else:
    # Impar
    print(f'O número {n} é impar.')
