from random import randint

cont = 0

while True:
    pc = randint(0, 10)
    jogador = int(input('Digite um valor: '))
    parimpar = str(input('Par ou Ímpar? [P/I]:')).upper().strip()[0]
    if (jogador + pc) % 2 == 0:
        if parimpar == 'P':
            print(f'Você jogou {jogador} e o computador {pc}. Total de {jogador + pc} DEU PAR.')
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            cont = cont + 1
        # end-if
        else:
            print(f'Você jogou {jogador} e o computador {pc}. Total de {jogador + pc} DEU ÍMPAR.')
            break
        #end-else
    else:
        if parimpar == 'I':
            print(f'Você jogou {jogador} e o computador {pc}. Total de {jogador + pc} DEU ÍMPAR.')
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            cont = cont + 1
        # end-if
        else:
            print(f'Você jogou {jogador} e o computador {pc}. Total de {jogador + pc} DEU ÍMPAR.')
            break
        # end-else
    # end-else
#end-while
print('Você PERDEU!')
print(f'Total de {cont} vitórias para você.')
