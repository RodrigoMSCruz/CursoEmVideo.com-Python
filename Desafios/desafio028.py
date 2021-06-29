# Gera um número aleatório entre 0 e 5 e lê o número do usuário e diz se acertou ou não.

from random import randint

numusuario = int(input('Tente adivinhar e digite um número inteiro de 0 a 5 que gerei: '))

numpc = randint(0, 5)

if numusuario == numpc:
    print('Parabéns! Você adivinhou! O número é {}!!!.'.format(numusuario))
else:
    print('Errou! O número que eu gerei foi {} e o que você digitou foi {}.'.format(numpc,numusuario))

