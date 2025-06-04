# Python
# analise de alistamento militar

from time import sleep

name = input("Olá, eu sou seu assistente para o Alistamento Militar, primeiro, como gostaria de ser chamado? ")
age = input(f"\nOla, {name}, Qual a sua idade? ")

difference = 0
youngerAge = 18
message = " "

sleep(1)

if age.isdigit:
    
    age = int(age)

    print(f"\nAnalisando\r", end = "")
    sleep(0.5)
    print(f"Analisando.\r", end = "")
    sleep(0.6)
    print(f"Analisando..\r", end = "")
    sleep(0.7)
    print(f"Analisando...")
    sleep(1)

    if age < youngerAge:
        
        difference = youngerAge - age
        year = "anos"
        
        if difference <= 1:
            year = "ano"
        else:
            year = "anos"
        
        message = f"ainda irá fazer o Alistamento Militar em {difference} {year}!"

    elif age > youngerAge:
        
        difference = age - youngerAge
        year = "anos"
        
        if difference <= 1:
            year = "ano"
        else:
            year = "anos"
        
        message = f"já fez o Alistamento Militar a {difference} {year}!"

    elif age == youngerAge:
       
        message = f"esta na época do Alistamento Militar, desejo boa sorte!"

    print(f"\nEntão {name}, você {message}\n")

else:
    
    print("\nDigite uma idade válida!")