# Python
# Tipo de triângulo
from time import sleep

name = input("Olá eu serei seu assistente hoje, primeiro, qual o seu nome? ")
name = name.capitalize()

l1: float = float(input(f"\nOlá {name}, digite o tamanho da primeira reta: "))
sleep(1)
l2: float = float(input("\nAgora o da segunda:"))
sleep(1)
l3: float = float(input("\nE por fim o da terceira reta: "))

comp1: bool = l1 + l2 > l3
comp2: bool = l2 + l3 > l1
comp3: bool = l3 + l1 > l2

sleep(1)

print(f"\nAnalisando\r", end = "")
sleep(1)
print("Analisando.\r", end = "")
sleep(1.5)
print("Analisando..\r", end = "")
sleep(2)
print("Analisando...\r", end = "")
sleep(2.5)

if comp1 and comp2 and comp3:

    triangle = ""
    
    if l1 == l2 and l2 == l3:
        triangle = "equilátero"
    
    elif l1 != l2 and l2 != l3 and l1 != l3:
        triangle = "escaleno"
    
    else:
        triangle = "Isóceles"

    print(f"As retas {l1}, {l2} e {l3} formam um triângulo do tipo {triangle}!")

else:
    print(f'As retas {l1}, {l2} e {l3} não formam um triângulo!')

