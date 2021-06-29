# Gera uma tabuada de um número inteiro inserido pelo usuário.

n = int(input('Digite um número inteiro para gerar uma tabuada: '))
print('=' * 14)

for i in range(1, 11, 1):
    print('{} x {:2} = {}'.format(n, i, n*i))
print('=' * 14)