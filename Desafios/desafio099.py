from time import sleep
def maior(*vnum):
    print('=-'*30)
    print('Analisando os valores passados...', end='')
    for n in vnum:
        sleep(0.5)
        print(f'{n} ', end='')
    print()
    print(f'Foram informados {len(vnum)} ao todo.')

    maior = 0
    for n in vnum:
        if n > maior:
            maior = n
        #end-if
    #end-for
    print(f'O maior valor informado foi {maior}')
#end-def maior


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()