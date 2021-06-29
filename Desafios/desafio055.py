# Programa lê o peso de 5 pessoas e depois informa o mais leve e o mais pesado.

peso = [0, 0, 0, 0, 0]

for i in range(0,5,1):
    pesodigit = float(input('Digite o peso da pessoa nº{}: '.format(i+1)))
    peso[i] = pesodigit
# end-for
peso.sort()
print('O maior peso digitado é: {}'.format(peso[0]))
print('O menor peso digitado é: {}'.format(peso[4]))
