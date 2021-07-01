# Programa com uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador
# e quantos gols ele marcou. O programa é capaz de mostrar a ficha do jogador, mesmo que algum dado não
# tenha sido informado corretamente.

def ficha(nome='<desconhecido>', gols=0):
    return (f'O jogador {nome} fez {gols} gol(s) no campeonato.')
# end-def-ficha


nome = str(input('Nome do jogador: ')).strip()
gols = str(input('Número de gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome =='':
    print(ficha(gols=gols))
else:
    print(ficha(nome, gols))
