from math import sin, cos, tan, radians
an = float(input('Digite o angulo desejado: '))
seno = sin(radians(an))
cose = cos(radians(an))
tang = tan(radians(an))
print (f'O angulo de {an} tem o SENO de {seno:.2f}')
print (f'O angulo de {an} tem o COSENO DE {cose:.2f}')
print (f'O angulo de {an} tem a TANGENTE de {tang:.2f}')
