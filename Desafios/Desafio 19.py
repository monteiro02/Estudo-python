from random import choices
n1 = 1 #str(input('Primeiro aluno: '))
n2 = 2 #str(input('Segundo aluno: '))
n3 = 3 #str(input('Terceiro aluno: '))
n4 = 4 #str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
escolhido = choices(lista, k=1, weights=[0.01, 0.01, 0.75, 0.01])
print (f'O aluno escolhido foi {escolhido}')
