print('======DESAFIO 34 ======')
salario = float(input('Qual é o salário do funcionário? '))
if salario > 1250.00:
    novo = salario + ((salario / 100) * 10)
else:
    novo = salario + ((salario/100) * 15)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(salario, novo))