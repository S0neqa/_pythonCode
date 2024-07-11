n1 = float(input('digite a primeira nota: '))
n2 = float(input('digite a segunda nota: '))

m = (n1 + n2)/2

print(f'sua média foi {m:.1f}')

if m >= 6.0:
    print('sua média foi muito boa, parabéns!')
else:
    print('sua média foi ruim!! estude mais!')