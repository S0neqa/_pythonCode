velo = int(input('qual a velocidade em que o carro estava?'))
taxa = float(7.00)

if velo > 80:
    multa = float((velo-80)*taxa)
    txt = (f'seu carro estava a {velo}Km/h,\n'
            f'e a multa por Km execedido é de R${taxa:.2f}'
            f'\n\nSua multa a pagar é R${multa:.2f}')

    print(txt)
print('tenha um bom dia! Dirija com segurança!')

