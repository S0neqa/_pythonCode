print('Para saber quantos dolar pode comprar digite um valor no formato "0.00"! ')
valor = float(input('Qual o valor em reais? '))
dollar = 3.27
print(f'Para R${valor} você pode comprar US${round(valor * dollar, 3)}.\n'
      f'lembrando que R$1.00 dolar esta R${dollar}')
