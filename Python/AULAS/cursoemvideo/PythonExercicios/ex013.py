print('======DESAFIO 013 ======')
salario = float(input('Qual é o salário do funcionário? R$'))
novo = salario + (salario* 15/100)

print('O funcionário que ganhava R${}, com 15% de aumento, passa a receber R${:.2f}'.format(salario,novo))