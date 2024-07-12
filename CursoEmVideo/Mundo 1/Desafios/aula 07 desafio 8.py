valor = float(input('digite o valor em metros para a conversão: '))
km = (10 ** (-3))
hm = (10 ** (-2))
dam = (10 ** (-1))
dm = (10 ** 1)
cm = (10 ** 2)
mm = (10 ** 3)

print(f'olá, o valor {valor}m convertidos ficará:'
      f'\n{valor*km}km;'
      f'\n{valor*hm}hm;'
      f'\n{valor*dam}dam;'
      f'\n{valor}m;'
      f'\n{valor*dm}dm;'
      f'\n{valor*cm}cm;'
      f'\n{valor*mm}mm.')
