# Jogo de Jokenpo do usuário contra o computador.

from random import choice

jokenpo = ['Papel', 'Pedra', 'Tesoura']  # lista. Esse assunto será visto mais adiante.

print('-=-=-=-=-=-=-=Jokenpô-=-=-=-=-=-=-=-=')
print('Escolha entre Papel, Pedra e Tesoura!')
print('[ 0 ] - Papel;')
print('[ 1 ] - Pedra;')
print('[ 2 ] - Tesoura.')
print('-='*18)

escolha = int(input('Escolha do jogador [0 - 2]: '))
jogador = jokenpo[escolha]
pc = choice(jokenpo)

print('-='*18)
print('Você jogou {}.'.format(jogador))
print('Computador jogou {}.'.format(pc))

print('-='*15)

if pc == 'Papel':  # Se o jogador escolher PAPEL:
    if jogador == 'Papel':
        print('EMPATE! Ambos escolheram PAPEL!')
    elif jogador == 'Pedra':
        print('Você perdeu! Eu escolhi Papel e você Pedra!')
    elif jogador == 'Tesoura':
        print('Você ganhou! Eu escolhi Papel e você Tesoura!')
    # end-if-elif
# end-if
elif pc == 'Pedra':  # Se o jodagor escolher PEDRA:
    if jogador == 'Papel':
        print('Você ganhou! Eu escolhi Pedra e você Papel!')
    elif jogador == 'Pedra':
        print('EMPATE! Ambos escolheram PEDRA!')
    elif jogador == 'Tesoura':
        print('Você perdeu! Eu escolhi Pedra e você escolheu Tesoura!')
    # end-if-elif
# end-elif
elif pc == 'Tesoura':  # Se o jogador escolher TESOURA:
    if jogador == 'Papel':
        print('Você perdeu! Eu escolhi Tesoura e você escolheu Papel!')
    elif jogador == 'Pedra':
        print('Você ganhou! Eu escolhi Tesoura e você escolheu Pedra!')
    elif jogador == 'Tesoura':
        print('Empate! Ambos escolheram Tesoura!')
    # end-if-elif
# end-elif
