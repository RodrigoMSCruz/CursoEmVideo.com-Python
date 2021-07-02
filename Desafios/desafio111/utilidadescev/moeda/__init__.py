def aumentar(preco, taxa, format = False):
    res = preco + (preco * taxa/100)
    if format is False:
        return res
    else:
        return moeda(res)


def diminuir(preco, taxa, format = False):
    res = preco - (preco * taxa/100)
    if format is False:
        return res
    else:
        return moeda(res)

def dobro(preco, format = False):
    res = preco * 2
    if format is False:
        return res
    else:
        return moeda(res)


def metade(preco, format = False):
    res = preco / 2
    if format is False:
        return res
    else:
        return moeda(res)

def moeda(preco = 0 , moeda = 'R$'):
    return f'{moeda} {preco:.2f}'.replace('.',',')

def resumo(preco = 0, taxamais = 10, taxamenos = 5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado:      {moeda(preco)}')
    print(f'Dobro do preço:       {dobro(preco, True)}')
    print(f'{taxamais}% de aumento:       {aumentar(preco, taxamais, True)}')
    print(f'{taxamenos}% de redução:       {diminuir(preco, taxamenos, True)}')
    print('-' * 30)
