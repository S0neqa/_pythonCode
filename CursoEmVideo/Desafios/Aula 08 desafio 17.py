from math import sqrt

CO = float(input('qual o valor do cateto oposto? '))
CA = float(input('qual o valor do cateto adjacente? '))

# H = ((CO**2)+(CA**2))**(1/2)
H = sqrt(CO*CO+CA*CA)

print(f'a impotenusa é {H}')
