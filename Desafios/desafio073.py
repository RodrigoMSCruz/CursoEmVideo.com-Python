# Programa com uma  tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro
# de Futebol, na ordem de colocação. Que mostra: Os 5 primeiros times; Os últimos 4 colocados;
# Times em ordem alfabética e em que posição está o time da Chapecoense.
# (Programa escrito em 05/02/2021)

brasileirao = ('Internacional', 'Flamengo', 'Atlético-MG', 'São Paulo', 'Fluminense', 'Palmeiras', 'Grêmio',
               'Corínthians', 'Bragatino', 'Athletico-PR', 'Santos', 'Ceará SC', 'Atlético-GO', 'Fortaleza',
               'Vasco da Gama', 'Bahia', 'Sport Recife', 'Goiás', 'Coritiba', 'Botafogo')
print('=-'*25)
print('Os 5 primeiros times são:')
print(brasileirao[0:5])

print('=-'*25)
print('Os 4 últimos times são:')
print(brasileirao[16:20])
# print(brasileirao[-4:])

print('=-'*25)
print('Os 20 times em ordem alfabética são:')
print(sorted(brasileirao))

print('=-'*25)

# O texto do exercíco pedia a posição da Chapecoense no campeonato, sendo que esse time não estava na série A
# do brasileião quando esse código foi escrito, portanto substituí por minha conta o nome do time pelo do Sport.
# Se a Chapecoese estivesse no brasileirão na epoca, a linha abaixo comentada seria a válida.

# print(f'A Chapecoense está em {brasileirao.index("Chapecoense")+1}º lugar.')
print(f'O Sport está em {brasileirao.index("Sport Recife")+1}º lugar.')
