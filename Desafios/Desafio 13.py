from ssl import ALERT_DESCRIPTION_BAD_CERTIFICATE_STATUS_RESPONSE


s = float(input('Qual o salario do funcionario? R$'))
a = s * 15 / 100 #Pegue o valor multiplique pelo valor da porcentagem divida por 100.
r = s + a  #Pegue o salario e some pelo resultado da porcentagem.
print (f'Um funcionario que ganhava R${s:.2f}, com 15% de aumento, passa a receber R${r:.2f}')