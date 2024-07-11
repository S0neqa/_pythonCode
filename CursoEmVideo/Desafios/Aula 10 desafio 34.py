salario = int(input('Qual o seu salário para o reajuste? '))

if salario > 1250:
    nSalario = salario * 1.10
else:
    nSalario = salario * 1.15

print(f'Seu novo salário é de R${nSalario:.2f}')