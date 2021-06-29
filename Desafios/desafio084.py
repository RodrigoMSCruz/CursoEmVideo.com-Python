# Programa que lê o nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostra: Quantas pessoas foram cadastradas; Uma listagem com as
# pessoas mais pesadas; Uma listagem com as pessoas mais leves.

temp = []
principal = []

menor = maior = 0

while True:
    temp.append(str(input('Nome: ')))
    temp.append((float(input('Peso: '))))
    if len(principal) == 0:
            menor = maior = temp[1]
    else:
        if temp[1] < menor:
            menor = temp[1]
        elif temp[1] > maior:
            maior = temp[1]
        # end-if-elif
    # end-if-else
    principal.append(temp[:])  # Copia a lista "dado" para pessoas(principal).
    temp.clear()  # limpa dado. Como a lista foi copiada, não se perde o que foi copiado para "pessoas"(principal).
    while True:
        continuar = str(input('Deseja continuar cadastrando? [S/N]: ')).strip().upper()[0]
        if continuar in 'SN':
            break
        else:
            print('A resposta deve ser S para sim ou N para Não.')
        #end-if
    # end-while
    if continuar == 'N':
        break
    # end-if
#end-while

print(f'Ao todo, você cadastrou {len(principal)} pessoas.')
print(f'O menor peso foi {menor}. É o peso de: ', end='')
for p in principal:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
    # end-if
# end-for
print()
print(f'O maior peso foi {maior}.É o peso de: ', end='')
for p in principal:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
    # end-if
# end-for
