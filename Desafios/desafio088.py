# Programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos
# serão gerados e sorteia 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep

bilhete = []
palpites = []
numpalpites = int(input('Quantos palpites deseja? '))

for i in range(1, numpalpites + 1):
    while len(bilhete) < 6:
        chute = randint(1, 60)
        if chute not in palpites:
            bilhete.append(chute)
    # end-while
    bilhete.sort()
    palpites.append(bilhete[:])
    bilhete.clear()
# end-for

for i, p in enumerate(palpites):
    print(f'Palpite {i + 1}: {p}')
    sleep(1)
# end-for