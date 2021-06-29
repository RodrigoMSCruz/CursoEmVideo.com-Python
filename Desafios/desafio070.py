# Programa lê o nome e o preço de vários produtos e pergunta se o usuário deseja continuar.
# Ao final, deverá exibir:
# * O total gasto na compra;
# * Quantos produtos custam mais de R$ 1000,00;
# * Qual o nome do produto mais barato.

cont = total = cprodutos1000 = maisbarato = 0
cnomemaisbarato = ''

while True:
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço do produto: '))
    total = total + preco
    cont = cont + 1
    if preco > 1000.0:
        cprodutos1000 = cprodutos1000 + 1
    # end-if
    if cont == 1 or preco < maisbarato:
        cnomemaisbarato = nome
        maisbarato = preco
    # end-if
    while True:
        opcao = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
        if opcao in 'SN':
            break
        # end-if
    # end-while
    if opcao == 'N':
        break
    # end-if
# end-while

print(f'O total gasto na compra é R$ {total:.2f}.')
print(f'Produtos que custam mais de R$ 1000: {cprodutos1000}')
print(f'O nome do produto mais barato é: {cnomemaisbarato}')
