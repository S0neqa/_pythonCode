print('Te ajudarei a saber qual o novo preço do produto com 5% de desconto!'
      'Por favor insira o valor no formato "0.00"')
preco = float(input('Para isso qual o valor inteiro do produto?'))
desconto = float(1-0.05)

print(f'o produto com o valor de R${preco}\n'
      f'descontado 5% terá seu novo valor de R${preco*desconto}!')
