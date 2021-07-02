def aumentar(preco, taxa, formato=False):
    res = preco + (preco * taxa/100)
    if formato is False:
        return res
    else:
        return moeda(res)
    # end-if-else
# end-def-aumentar


def diminuir(preco, taxa, formato=False):
    res = preco - (preco * taxa/100)
    if formato is False:
        return res
    else:
        return moeda(res)
    # end-if-else
# end-def-diminuir


def dobro(preco, formato=False):
    res = preco * 2
    if formato is False:
        return res
    else:
        return moeda(res)
    # end-if-else
# end-def-dobro


def metade(preco, formato=False):
    res = preco / 2
    if formato is False:
        return res
    else:
        return moeda(res)
    # end-if-else
# end-def-metade


def moeda(preco=0, moeda='R$'):
    return f'{moeda} {preco:.2f}'.replace('.', ',')
# end-def-moeda


def resumo(preco=0, taxamais=10, taxamenos=5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado:      {moeda(preco)}')
    print(f'Dobro do preço:       {dobro(preco, True)}')
    print(f'{taxamais}% de aumento:       {aumentar(preco, taxamais, True)}')
    print(f'{taxamenos}% de redução:       {diminuir(preco, taxamenos, True)}')
    print('-' * 30)
# end-def-resumo
