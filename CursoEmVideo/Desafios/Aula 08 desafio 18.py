from math import radians, sin, cos, tan

ang = radians(int(input('angulo: ')))

seno = sin(ang)
cosseno = cos(ang)
tg = tan(ang)

print(f'o seno é {seno:.2f}'
      f'\no cosseno é {cosseno:.2f}'
      f'\ne a tangente é {tg:.2f}')

