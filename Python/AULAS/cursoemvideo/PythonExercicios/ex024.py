print('======DESAFIO 24 ======')
cid = str(input('Em que cidade você nasceu? ')).strip()
print('SANTO' in cid[:5].upper())
print(cid[:5].upper() == 'SANTO')
separa = cid.split()
print('SANTO' in separa[0].upper())

