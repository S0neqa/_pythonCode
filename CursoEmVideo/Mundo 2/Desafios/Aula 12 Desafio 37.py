# Python code
# desafio 37 do mundo 2 do curso em video

from time import sleep

number = input(f"\nOlá, {input(str("Primeiro, qual o seu nome? "))} tudo bem?, eu serei seu assitente de conversão númerico,\nagora escreva um número inteiro que queira converter ")
sleep(0.5)

if number.isdigit():

    number = int(number)

    print(f"\nO número {number} é uma boa escolha, ok, vamos lá!!")
    sleep(1)

    conversion = str(input(f"\nPara qual base você quer converter? \n\nBinário (B), \nOctal (O), \nHexadecimal (H),\n \nDigite A letra respectiva para a conversão: "))
    sleep(2)

    result = " "
    choose = " "

    if conversion.upper() == "B":
        
        result = bin(number)[2:]
        choose = "Binario"

    elif conversion.upper() == "H":

        result = hex(number)
        choose = "Hexadecimal"

    elif conversion.upper() == "O":

        result = oct(number)
        choose = "Octal"

    else:
        result = " "

    print(f"\nConvertendo\r", end = "")
    sleep(0.5)
    print(f"Convertendo.\r", end = "")
    sleep(0.6)
    print(f"Convertendo..\r", end = "")
    sleep(0.7)
    print(f"Convertendo...\r", end = "")
    sleep(0.8)
    
    if conversion.upper() == "B" or conversion.upper() == "H" or conversion.upper() == "O":
        
        print(f"\nO seu número convertido para {choose} ficou {result}")

    else:
        print("\nSelecione uma opção válida!")

else:
    print("\nDigite um valor válido")