num = str(input('Digite um número de 0 a 9999: '))

if len(num) == 4:
    print(f"""Dado ao número {num}
    a unidade é {num[3]};
    a dezena é {num[2]};
    a centena é {num[1]};
    e a unidade de milhar é {num[0]}.""")

elif len(num) == 3:
    print(f"""Dado ao número {num}
    a sua unidade é {num[2]};
    a sua dezena é {num[1]};
    a sua centena é {num[0]};
    e a sua unidade de milhar é 0.""")

elif len(num) == 2:
    print(f"""Dado ao número {num}
    a sua unidade é {num[1]};
    a sua dezena é {num[0]};
    a sua centena é 0;
    e a sua unidade de millhar é 0.""")

elif len(num) == 1:
    print(f"""Dado ao número {num}
    a sua unidade é {num};
    sua dezena é 0;
    a sua centena é 0;
    e a sua unidade de milhar é 0.""")

else:
    print('Por favor digite um número válido')
