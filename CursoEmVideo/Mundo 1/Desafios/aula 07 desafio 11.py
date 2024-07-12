print('Olá, iremos te ajudar a saber quantas tintas você precisará para pintar uma parede\n'
      'digite primeiro os valores pedidos no formato "0.00 metros"')
largura = float(input('qual a largura da parede? '))
altura = float(input('qual a altura da parede? '))
area = largura*altura
tinta = area/2
print(f'Para uma parede de {largura}m x {altura}m temos uma área de {area}m²,\n'
      f'tendo em vista que cada litro de tinta pode pintar até 2m² então \n'
      f'para pintar essa parede precisaremos de {tinta} litros de tinta!')
