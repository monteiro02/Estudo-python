d = int(input('Quantos dias alugado? '))
km = float(input('Quantos km percorridos? '))
p = (d * 60) + (km * 0.15)
print (f'O total a pagar é de R${p:.2f}')