# Programa que gerencia o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador
# e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo
# isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = {}
partidas = []

jogador['nome'] = str(input('Nome do Jogador: '))
njogos = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for i in range(1, njogos + 1, 1):
    gols = int(input(f'Quantos gols na partida {i}? '))
    partidas.append(gols)
# end-for
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
partidas.clear()

for k, v in jogador.items():
    print(f'O campo {k} tem o valor: {v}')
# end-for
print('')
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} jogos.')
print('Relação de gols:')
for k, v in enumerate(jogador['gols']):
    print(f'No jogo {k + 1}, o jogador {jogador["nome"]} fez {v} gols.')
# end-for
