# Aprimoramento do desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de
# visualização de detalhes do aproveitamento de cada jogador.

time = []
jogador = {}
partidas = []

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    njogos = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for i in range(1, njogos + 1, 1):
        gols = int(input(f'Quantos gols na partida {i}? '))
        partidas.append(gols)
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    partidas.clear()
    time.append(jogador.copy())
    while True:
        resposta = str(input('Quer cadastrar mais jogadores? [S/N]: ')).upper()[0]
        if resposta in 'SN':
            break
        print('Resposta inválida. Responda com S ou N.')
    # end-while True
    if resposta == 'N':
        break
# end-while True

print('-='*50)
print('Cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end= '')
print()

print('-='*50)
for k, v in enumerate(time):
    print(f'{k:>3}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-='*50)

while True:
    busca = int(input('Digite o código do jogador para mais dados. (999 para sair.) '))
    if busca == 999:
        break
    if busca > len(time):
        print(f'Erro! Código para jogador {busca} inexistente.')
    else:
        print(f'Mostrando dado do jogador {time[busca]["nome"]}')
        for i, g in enumerate(time[busca]["gols"]):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-='*50)
# nd-while
