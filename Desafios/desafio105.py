def notas(*num, sit=False):
    """
    Retorna um dicionário com a quantidade de notas, a maior nota, a menor nota, a média e a situação(opcional)
    :param num: Notas dos alunos
    :param sit: Situação. Se true,, mostra a situação conforme a média. Se false, não mostra a situação.
    :return: dicionário com a quantidade de notas, a maior, a menor, a média e a situação(Opcional).
    """

    total = len(num)
    maior = max(num)
    menor = min(num)
    media = sum(num) / total
    if sit:
        if media >=7:
            situacao = 'Boa'
        if 5 < media < 7:
            situacao = 'Razoável'
        if media <=5:
            situacao = 'Ruim'
    # end-if
    if sit == True:
        return {'total': total,
                'maior': maior,
                'menor': menor,
                'média': media,
                'situação': situacao}
    else:
        return {'total': total,
                'maior': maior,
                'menor': menor,
                'média': media}
    # end-if-else
# end-def notas


print(notas(4.5, 5.5, 7, 8, 2.5, 4, sit=True))
print(notas(4.5, 5.5, 7, 8, 2.5, 4))
help(notas())
