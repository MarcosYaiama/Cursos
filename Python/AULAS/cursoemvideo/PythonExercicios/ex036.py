print('======DESAFIO 36 ======')
valor_casa = float(input('Valor da casa: R$'))
salario_comprador = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))

meses = anos * 12
parcela = valor_casa/ meses

minimo = salario_comprador/100 * 30
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de'
      ' R${:.2f}'.format(valor_casa, anos,parcela))

if(parcela > minimo):
    print('Empréstimo \033[1;31mNEGADO\033[m')
else:
    print('Empréstimo \033[1;32mCONCEDIDO\033[m')