def aumentar(preco, taxa, formato=False):
    res = preco + (preco * taxa/100)
    if formato is False:
        return res
    else:
        return moeda(res)


def diminuir(preco, taxa, formato=False):
    res = preco - (preco * taxa/100)
    if formato is False:
        return res
    else:
        return moeda(res)


def dobro(preco, formato=False):
    res = preco * 2
    if formato is False:
        return res
    else:
        return moeda(res)


def metade(preco, formato=False):
    res = preco / 2
    if formato is False:
        return res
    else:
        return moeda(res)


def moeda(preco=0, moeda='R$'):
    return f'{moeda} {preco:.2f}'.replace('.', ',')
