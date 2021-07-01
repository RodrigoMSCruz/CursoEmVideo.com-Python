# Programa que contém uma função(def) chamada fatorial que deve retornar o resultado do fatorial
# de um número passado por parâmetro. Deve ter também a capacidade de mostrar o cálculo do resultado
# dependendo de outro parâmetro ser passado como True ou False.

def fatorial(n, show=False):
    """
    :param n: Número a ser calculado o fatorial
    :param show: Se True, mostra o processo de cálculo, se False, mostra apenas o resultado
    :return: Retorna todo o cálculo e o resultado ou apenas o resultado, conforme o paramêtro show.
    """
    fat = 1
    for i in range(n, 0, -1):
        fat = fat * i
        if show:
            if i > 1:
                print(f'{i} x ', end='')
            if i == 1:
                print(f'{i} = ', end='')
        # end-if
    # end-for
    return fat
# end def-fatorial


n = int(input('Digite o valor a calcular o fatorial: '))
opcao = str(input('Deseja ver o processo de cálculo? [S/N]: ')).upper()[0]
if opcao == 'S':
    print(fatorial(n, True))
else:
    print(fatorial(n, False))
# end-if
help(fatorial)
