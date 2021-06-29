# Converte para Fº uma temperatura em Cº inserida pelo usuário.
tempc = float(input('Informe a temperatura em Cº:'))
temf = ( ( 9 * tempc ) / 5 ) + 32
print('A temperatura de {}Cº corresponde a {}Fº.'.format(tempc, temf))
