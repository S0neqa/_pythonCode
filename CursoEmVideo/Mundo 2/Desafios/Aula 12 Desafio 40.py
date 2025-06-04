# Python
# Analise de notas da escola

from time import sleep

name = input("Olá, tudo bem? eu sou seu assistente escolar, primeiro, me diga o seu nome: ")

grade1 = input(f"\nOlá {name}, que nome bonito! bom, vamos lá, qual a sua primeira nota? ")
grade2 = input(f"\nCerto, {grade1}, e agora, qual a segunda nota? ")

if grade1.isdigit and grade2.isdigit:

    grade1 = int(grade1)
    grade2 = int(grade2)
    
    average = float((grade1+grade2)/2)
    
    print("\nCalculando\r",  end= "")
    sleep(1)
    
    print("Calculando.\r",   end= "")
    sleep(1)
    
    print("Calculando..\r",  end= "")
    sleep(1)
    
    print("Calculando...")
    sleep(3)

    message = ""

    if average < 5.0:

        message = "portanto você foi REPROVADO! Boa sorte na próxima"
    
    elif average >= 5.0 and average <= 6.9:

        message = "portanto você terá de fazer RECUPERAÇÃO! Boa sorte"
    
    elif average > 7.0:
        
        message = "portanto você foi APROVADO! Meus parabéns"
    
    print(f"\n{name}, sua média foi de {average}, {message}!\n")

        
