l1: float = float(input('Digite o tamanho da primeira reta: '))
l2: float = float(input('Digite o da segunda:'))
l3: float = float(input('Agora o da terceira reta: '))

comp1: bool = l1 + l2 > l3
comp2: bool = l2 + l3 > l1
comp3: bool = l3 + l1 > l2

if comp1 and comp2 and comp3:
    print(f'As retas {l1}, {l2} e {l3} formam um triângulo!')
else:
    print(f'A retas {l1}, {l2} e {l3} não formam um triângulo!')
