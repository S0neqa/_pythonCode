nome = str(input('Qual o seu nome completo? '))
nomeSeparado = nome.split()

tudoMaiusculo = nome.upper()

tudoMinusculo = nome.lower()

contLetras = len(''.join(nomeSeparado))

cont1Nome = len(nomeSeparado[0])

print(f"""Olá {nome.title()}, segue as informações:
Seu nome tudo em maiusculo: {tudoMaiusculo};
Seu nome tudo em minusculo: {tudoMinusculo};
Numero de letras no seu nome (desconsiderando espaços): {contLetras}
Numero de letras do seu primeiro nome: {cont1Nome}""")
