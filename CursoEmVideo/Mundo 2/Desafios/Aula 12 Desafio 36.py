from tkinter import *
# comando da biblioteca para auxilio do tempo
from time import sleep
tax = 0.3

print("Olá, eu sou assistente bancário e irei te ajudar no seu empréstimo,\n então irei te fazer algumas perguntas antes da analise!")
sleep(1.5)

print("")

# Valores fornecidos para o calculo
value = int(input("Primeiro, qual o valor da casa? "))
print("")

wage = int(input("Segundo, qual o seu salário? "))
print("")

time = int(input("Por fim, em quanto tempo em anos você planeja pagar a casa? "))
print("")


# "tela" de carregando
print("Carregando\r", end="")
sleep(1)
print("Carregando.\r", end="")
sleep(1)
print("Carregando..\r", end="")
sleep(1)
print("Carregando...")
sleep(2)

print("")

# calculos
installment = int(value/time)
limit = int(wage*0.3)

print(f"Você ganha R${wage}, então o limite de 30% do seu salário é de R${limit}")
print("")
sleep(1)


# suspense
print(f"O seu financiamento é de R${installment}, então\r", end="")
sleep(1.5)
print(f"O seu financiamento é de R${installment}, então.\r", end="")
sleep(1.5)
print(f"O seu financiamento é de R${installment}, então..\r", end="")
sleep(1.5)
print(f"O seu financiamento é de R${installment}, então...")
sleep(1.5)

print("")

# Teste com interface
janela = Tk()
janela.title("Resultado")
janela.geometry("220x180")


# condições para compra
if installment < limit:
    textoParaResultasdo = f"O seu financiamento esta liberado, parabéns pela compra do seu imvóvel"
    
    print(f"O seu financiamento esta \033[1;32m liberado \033[0;30m, parabéns pela compra do seu imvóvel")

    textoResultado = Label(janela, text = textoParaResultasdo)
    textoResultado.grid(column=0, row=0, padx=10, pady=10)

else:

    textoParaResultasdo = "Infelizmente o financiamento não foi liberado"
    print(textoParaResultasdo)
    textoResultado = Label(janela, text = textoParaResultasdo)
    textoResultado.grid(column=0, row=0, padx=10, pady=10)

print("")

janela.mainloop()