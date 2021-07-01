# Programa que pede uma função "def" que recebe vários números(ou nenhum) e informa qual é o maior.

from time import sleep


def maior(*vnum):
    print('=-'*30)
    print('Analisando os valores passados...', end='')
    for n in vnum:
        sleep(0.5)
        print(f'{n} ', end='')
    # end-for
    print()
    print(f'Foram informados {len(vnum)} ao todo.')

    maiorn = 0
    for n in vnum:
        if n > maiorn:
            maiorn = n
        # end-if
    # end-for
    print(f'O maior valor informado foi {maiorn}')
# end-def maior


# Programa Principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
