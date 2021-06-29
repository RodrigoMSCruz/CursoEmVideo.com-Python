# Programa que lê o valor de um produto e o mostra com 5% de desconto.
preco = float(input('Digite o valor do produto: R$ '))
precodesconto = preco - (preco * 0.05) #Aplicar os 5% de desconto.
#precodesconto = preco - (preco * (5/100))
print('O produto possui o preço de R$ {:.2f}\nCom o desconto de 5%, o valor fica: R$ {:.2f}'.format(preco,precodesconto))
