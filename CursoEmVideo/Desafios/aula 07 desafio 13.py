print('Para descobrir o seu novo salário com aumento de 15% digite seu salario atual \n'
      'no formato "0000.00"')

salario = float(input('qual o salário atual? '))
aumento = float(1+0.15)

mensagem = (f'O salário de R${salario} com um aumento de 15% terá seu novo valor em\n'
            f'R${round(salario*aumento, 2)} !')

print(mensagem)
