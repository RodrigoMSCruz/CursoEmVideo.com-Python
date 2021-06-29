# Conversão de R$ inserido pelo usuário para US$, tendo com a cotação do dólar a R$ 3,27.
dinreal = float(input('Digite o valor que você possui em R$: '))
dindolar = (dinreal / 3.27)
print('O valor R$ {} que possui, corresponde a US$ {:.2f} pela cotação de US$=R$3,27.'.format(dinreal, dindolar))
