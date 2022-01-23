# t = int (input('Quantas tampinhas tem: '))
# v = t * 0.10
# print (f'O valor de {t} tampinhas é R${v:.2f} ')

l = float(input('Largura da parede: '))
a = float(input('Altura da parede: '))
p = l * a

print (f'Sua parede tem a dimenção de {l}x{a} e sua area é de {p}m² ')
t = p / 2
print (f'Para pintar a parede, voce precisara de {t}l de tinta.')
