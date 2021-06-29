# Programa onde o usuário pode digitar vários valores numéricos e cadastrá-los em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os
# valores únicos digitados, em ordem crescente.

valores = []

while True:
    valor = int(input('Digite um valor: '))
    if valor in valores:
        print('Valor já existente! Valores replicados não são admitidos.')
    else:
        valores.append(valor)
    # end-if-else
    while True:
        resposta = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
        if resposta in 'SN':
            break
        else:
            print('ERRO! Responda apenas com S para sim e N para não.')
        # end-if-else
    # end-while
    if resposta == 'N':
        break
    # end-if
# end-while
valores.sort()
print(f'Você digitou os valores: {valores}.')
