# Lê a distância da viagem inserida pelo usuário e calcula o valor da passagem.
# Sabendo que o valor por km é 0,50 para menor ou igual a 200 km e R$ 0,45 para maiores que 200 km.

dist = float(input('Digite a distância em km da viagem: '))
if dist <= 200.0:
    valor = dist * 0.5
else:
    valor = dist * 0.45
# valor = dist *0.50 if dist <= 200 else dist * 0.45
print('O valor da passagem é R$ {:.2f}.'.format(valor))

