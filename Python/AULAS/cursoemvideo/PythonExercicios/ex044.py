print('{:=^40}'.format(' DESAFIO 44 '))
preco_normal = float(input('\033[1;30mPreço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')

condicao = int(input('Qual é a opção? '))
opcao_valida = True
preco = preco_normal
if condicao == 1:
    preco = preco_normal - ((preco_normal/100) * 10)
elif condicao == 2:
    preco = preco_normal - ((preco_normal/100) * 5)
elif condicao == 3:
    preco = preco_normal
    parcelas = preco / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcelas))
elif condicao == 4:
    parcelas = int(input('Quantas parcelas? '))
    preco = preco_normal + ((preco_normal / 100) * 20)
    valor_parcela = preco/parcelas
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(parcelas,valor_parcela))
else:
    print('\033[1;31;40m OPÇÃO INVÁLIDA \033[30m de pagamento. Tente novamente!')
    opcao_valida = False
if(opcao_valida):
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco_normal,preco))