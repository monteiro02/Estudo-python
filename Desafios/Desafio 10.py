real = float(input('Quanto de dinheiro voce tem? R$'))
dolar = real / 5.46
iene = real / 0.048
libra = real / 7.50
euro = real / 6.33
print (f'Com R$ {real:.2f} você pode comprar \nUS$ {dolar:.2f} \n¥ {iene:.2f} \n£ {libra:.2f} \n€ {euro:.2f}')
