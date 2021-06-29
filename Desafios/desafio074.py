# Programa que gera 5 números aleatórios e coloca-os em uma tupla. Depois disso, mostra a listagem
# de números gerados e também indica o menor e o maior valor que estão na tupla.

from random import randint

menor = maior = 0
numeros = (randint(0, 100),
           randint(0, 100),
           randint(0, 100),
           randint(0, 100),
           randint(0, 100)
           )

print('=-'*25)
print('Os numeros gerados são:')
for n in numeros:
    print(f'{n} - ', end='')
# end-for
print('FIM')

print('=-'*25)
print(f'O menor número gerado foi: {min(numeros)}.')
print(f'O maior número gerado foi: {max(numeros)} .')
print('=-'*25)
