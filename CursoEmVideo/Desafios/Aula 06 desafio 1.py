dado = input('digite algo: ')
alpha = dado.isalpha()
alfaNum = dado.isalnum()
print(f'A entrada {dado} tem segue algumas informações como:')
print(f'O valor {dado} é do tipo {type(dado)}')
print(f'Letra maiuscula: {dado.isupper()}')
print(f'É do alfabeto: {dado.isalpha()}')
print(f'É um número: {dado.isalnum()}')
print(f'É da tabela ASCII: {dado.isascii()}')
print(f'É um número decimal: {dado.isdecimal()}')
print(f'É um digito: {dado.isdigit()}')
print(f'É númerico: {dado.isnumeric()}')
print(f'Ou se é um espaço: {dado.isspace()}')
