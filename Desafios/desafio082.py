# Programa que lê vários números e coloca em uma lista. Depois disso, crie duas listas extras que
# vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final,
# mostra o conteúdo das três listas geradas.

todosn = []
pares = []
impares = []

while True:
    n = int(input('Digite um valor: '))
    todosn.append(n)
    while True:
        continua = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
        if continua in 'SN':
            break
        else:
            print('Digite S para sim e N para não.')
        # end if-else
    # end-while
    if continua == 'N':
        break
    # end-if
# end-while

for n in todosn:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    # end-if-else
# end-for

print(f'Todos os valores digitados: {todosn}.')
print(f'Todos os pares: {pares}.')
print(f'Todos os ímpares: {impares}.')
