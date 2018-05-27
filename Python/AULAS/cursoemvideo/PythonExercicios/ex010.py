print('======DESAFIO 010 ======')
real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 3.305
libra = real / 4.269
euro  = real / 3.751

print('Com R${:.2f} você pode comprar:'.format(real))
print('U${:.2f}'.format(dolar))
print('E${:.2f}'.format(euro))
print('L${:.2f}'.format(libra))