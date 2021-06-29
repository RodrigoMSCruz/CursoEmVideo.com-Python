# Calcula o valor de um aluguel de carro com base no tempo em dias e na distância em km percorridos em km.
# O valor é R$ 60 por dia e R$ 0,15 por km rodado.
qkm = float(input('Qual a quilometragem rodada pelo veículo? '))
qdia = int(input('Qual o tempo em dias que o carro foi alugado? (Inteiro) '))
valor = (qkm * 0.15) + (qdia * 60)
print('O valor final é: R$ {:.2f}'.format(valor))
