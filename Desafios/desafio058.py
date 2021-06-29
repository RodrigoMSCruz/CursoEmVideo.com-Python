# Gera um número aleatório entre 0 e 10 e lê o número do usuário continuamente até o usuário acertar
# e exibe quantas tentativas foram nacessárias.
# Versão melhorada do desafio028.

from random import randint

continua = True
c = 0
while continua == True:
    numpc = randint(0, 10)
    numusuario = int(input('Gerei um número de 0 a 10. Qual o seu chute? '))
    c = c + 1
    if numusuario == numpc:
        print('Você adivinhou! Você precisou de {} tentativas para acertar!'.format(c))
        continua = False
    else:
        print('Errou! O número que eu gerei foi {}. Vou gerar outro número!'.format(numpc))
    #end-if-else
# end-while
