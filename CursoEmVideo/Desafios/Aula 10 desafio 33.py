n1 = int(input('digite o primeiro número: '))
n2 = int(input('digite o segundo número: '))
n3 = int(input('digite o terceiro número: '))

# num = [n1, n2, n3]

# bigger = max(num)
# lower = min(num)

# print(f'dentre os números {num}, \no número {bigger} é o maior \ne o {lower} é o menor!')

menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print(f'O maior número digitado foi {maior}!')
print(f'O menor número digitado foi {menor}!')