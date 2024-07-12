graus = float(input('Qual a temperatura em °C você quer saber em °F? '))

conv = ((graus * 9) / 5) + 32
msg = f'a temperatura de {graus:.0f}°C convertida fica {conv}°F'

print(msg)
