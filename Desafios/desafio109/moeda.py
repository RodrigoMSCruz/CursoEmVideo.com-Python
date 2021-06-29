def aumentar(preco, taxa, format = False):
    res = preco + (preco * taxa/100)
    if format is False:
        return res
    else:
        return moeda(res)


def diminuir(preco, taxa, format = False):
    res = preco - (preco * taxa/100)
    if format is False
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