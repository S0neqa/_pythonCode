dado = input('digite algo: ')
alpha = dado.isalpha()
alfaNum = dado.isalnum()

Cores = {
    'limpar': '\033[m',
    'verde': '\033[32;40m',
    'azul': '\033[36;40m'}

print(f'A entrada {Cores['azul']}{dado}{Cores['limpar']} tem segue algumas informações como:')
print(f'O valor {Cores['azul']}{dado}{Cores['limpar']} é do tipo {Cores['verde']}{type(dado)}{Cores['limpar']}')

print(f'Letra {Cores['azul']}maiuscula{Cores['limpar']}: {Cores['verde']}{dado.isupper()}{Cores['limpar']}')
print(f'É do {Cores['azul']}alfabeto{Cores['limpar']}: {Cores['verde']}{dado.isalpha()}{Cores['limpar']}')
print(f'É um {Cores['azul']}número{Cores['limpar']}: {Cores['verde']}{dado.isalnum()}{Cores['limpar']}')
print(f'É da {Cores['azul']}tabela ASCII{Cores['limpar']}: {Cores['verde']}{dado.isascii()}{Cores['limpar']}')
print(f'É um {Cores['azul']}número decimal{Cores['limpar']}: {Cores['verde']}{dado.isdecimal()}{Cores['limpar']}')
print(f'É um {Cores['azul']}digito{Cores['limpar']}: {Cores['verde']}{dado.isdigit()}{Cores['limpar']}')
print(f'É {Cores['azul']}númerico{Cores['limpar']}: {Cores['verde']}{dado.isnumeric()}{Cores['limpar']}')
print(f'Ou se é um {Cores['azul']}espaço{Cores['limpar']}: {Cores['verde']}{dado.isspace()}{Cores['limpar']}')
