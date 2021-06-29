# Lê a velocidade inserida pelo usuário e exibe se foi multado e qual valor da multa.
# Valor da multa é de R$ 7 por km/h excedido de 80 km/h.

vel = float(input('Qual a velocidade do veículo? '))
if vel <= 80.0:
    print('OK!')
else:
    multa = (vel-80)*7
    print('Você será multado! Valor da multa: R$ {:.2f}.'.format(multa))
