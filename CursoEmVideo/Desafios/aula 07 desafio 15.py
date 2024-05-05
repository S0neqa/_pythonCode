dias = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Por quantos km o carro andou? '))

Valor = float((dias * 60.00) + (km * 0.15))

msg = (f'Para o carro alugado por {dias} dias e que rodou por {km} km '
       f'\no total a ser pagar será de R${Valor:.2f}!')

print(msg)
