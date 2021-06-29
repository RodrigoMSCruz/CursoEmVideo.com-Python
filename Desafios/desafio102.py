def fatorial(n, show=False):
    """
    :param n: Número a ser calculado o fatorial
    :param show: Se True, mostra o processo de cálculo, se False, mostra apenas o resultado
    :return: Retorna todo o cálculo e o resultado ou apenas o resultado, conforme o paramêtro show.
    """
    fat = 1
    resp = ''
    for i in range(n, 0, -1):
        fat = fat * i
        if show == True:
            if i > 1:
                print(f'{i} x ', end ='')
            if i == 1:
                print(f'{i} = ', end = '')
        #end-if
    #end-for
    return resp

n = int(input('Digite o valor a calcular o fatorial: '))
opcao = str(input('Deseja ver o processo de cálculo? [S/N]: ')).upper()[0]
if opcao == 'S':
    print(fatorial(n, True))
else:
    print(fatorial(n, False))
help(fatorial)