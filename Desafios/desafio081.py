# Programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostra: Quantos números foram digitados; A lista de valores, ordenada de forma decrescente;
# Se o valor 5 foi digitado e está ou não na lista.

listan = []

while True:
    num = int(input('Digite um valor: '))
    listan.append(num)
    while True:
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
        if continuar in 'SN':
            break
        else:
            print('Responda S para sim ou N, para não.')
        # if-else
    # end-while
    if continuar == 'N':
        break
    # end-if
# end-while

print(f'Foram digitados {len(listan)} números.')
listan.sort(reverse=True)
print(f'A lista em ordem decrescente é: {listan}.')
if 5 in listan:
    print('O valor 5 está na lista.')
else:
    print('O valor 5 não está na lista.')
# end-if-else
