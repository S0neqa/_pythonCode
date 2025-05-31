# Python
# Leitura de dois valores comparando os dois

from time import sleep

name = input("Olá, eu sou seu assitente comparador de números inteiros, e irei te ajudar hoje,\nComo gostaria de ser chamado? ")
sleep(0.5)

number1 = input(f"\nOlá {name}, agora me digite o primeiro número inteiro para comparação: ")
sleep(0.5)

number2 = input(f"Muito bem, agora o segundo: ")
sleep(0.5)

if number1.isdigit() and number2.isdigit():
    
    number1 = int(number1)
    number2 = int(number2)

    print(f"\nInteressante, o vamos então iremos comparar o número {number1} e o {number2}")
    sleep(1)

    print(f"\nComparando\r", end = "")
    sleep(0.5)
    print(f"Comparando.\r", end = "")
    sleep(0.6)
    print(f"Comparando..\r", end = "")
    sleep(0.7)
    print(f"Comparando...\n", end = "")
    sleep(2)

    if number1 > number2:
        
        print(f"\nO número {number1} é maior que o {number2}!")
    
    elif number1 < number2:
        
        print(f"\nO número {number1} é menor que o {number2}!")
    
    elif number1 == number2:

        print(f"\nNão existe difereça, os dois são iguais!")

else:
    print(f"\nDigite dois números válidos")