nome = input('Digite seu nome: ').title().strip()
nomeSeparado = nome.split()

primeiro = nomeSeparado[0]
ultimo = nomeSeparado[len(nomeSeparado) - 1]

print(f'olá {nome}, '
      f'\nseu primeiro nome é {primeiro};'
      f'\ne o ultimo é {ultimo}.'
      f'\né um prazer {primeiro + ' ' + ultimo}')
