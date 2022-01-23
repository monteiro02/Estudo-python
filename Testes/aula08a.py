#import doce: ira importar todos os itens da biblioteca
#from doce import bala: ira importar um item especifico da biblioteca

#quando se instala o python ja vem instalado a biblioteca "math" mas não vem importada


#funcionalidade:
#"math"
#ceil              FAZ UM ARRENDONDAMENTO PARA CIMA
#floor             FAZ UM ARRENDONDAMENTO PARA BAIXO
#trunc             VAI TRUNCAR O NUMERO, ELIMINAR DA VIRGULA PARA FRENTE
#pow               POTENCIA
#sqrt              RAIZ QUADRADA
#factorial         CALCULO FATORIAL

#'import math'
#'from math import sqrt, ceil'


from math import sqrt, floor
num = int(input('Digite um número:'))
raiz = sqrt(num)
print (f'A raiz de {num} e igual a {floor(raiz):.2f}')


