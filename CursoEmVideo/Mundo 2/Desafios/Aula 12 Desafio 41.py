# Python
# Categoria para idade de nadadores

from time import sleep

print("Olá, nós somos a Confederação Nacional de Natação!")
sleep(0.8)

# Entrada das variaveis
name = input("\nPrimeiro, qual o seu nome? ")
name = name.capitalize()
age = int(input(f"\nOlá {name}, para definir sua categória me informe a sua idade: "))

# Carregamento
print(f"\nAnalisando\r", end = "")
sleep(0.5)
print(f"Analisando.\r", end = "")
sleep(0.6)
print(f"Analisando..\r", end = "")
sleep(0.7)
print(f"Analisando...")
sleep(1)

# Categorias
categories = [
    "Mirim",
    "Infantil",
    "Junior",
    "Sênior",
    "Master"
]

# Variável para guardar a categoria
category = ""

# Definição de categorias 
if age <= 9:
    category = categories[0]

elif age > 9 and age <= 14:
    category = categories[1]

elif age > 14 and age <= 19:
    category = categories[2]

elif age > 19 and age <= 20:
    category = categories[3]

elif age > 20:
    category = categories[4]

print(f"\nEntão {name}, com base na sua idade sua categoria é {category}, meus parabéns e boa sorte!")