distancia = int(input('Qual a distancia da viagem? '))

if distancia < 200:
    taxa = float(0.50)
    valor = distancia * taxa
    print(f'Você irá pagar R${valor:.2f}')
else:
    taxa = float(0.45)
    valor = distancia * taxa
    print(f'Você irá pagar R${valor:.2f}')
