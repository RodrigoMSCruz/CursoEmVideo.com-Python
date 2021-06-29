# Programa com uma função chamada contador(), que recebe três parâmetros: início, fim e passo.
# O programa tem que realizar três contagens através da função criada:
# de 1 até 10, de 1 em 1; de 10 até 0, de 2 em 2; uma contagem personalizada.

from time import sleep
def contagem(i, f, p):
    if i > f:
        ff = f - 1
        p = p*(-1)
    else:
        ff = f + 1
    #end-if-else
    if p == 0:
        p = 1
    #end-if
    print(f'Contagem de {i} até {f} de {p} em {p}:')
    for c in range(i, ff, p):
        print(f'{c} ', end='')
        sleep(0.5)
    #end-for
    print('FIM!')
#end-def


contagem(1, 10, 1)
contagem(10, 0, 2)

print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Ínicio: '))
fim = int(input('Final: '))
passo = int(input('Passo: '))
contagem(inicio, fim, passo)