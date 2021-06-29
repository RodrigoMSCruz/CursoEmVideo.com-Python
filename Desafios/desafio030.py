# Lê um número inserido pelo usuário e diz se é par ou ímpar.

num = int(input('Digite um número: '))

if num % 2 == 0:
    #Checa se o número é par ou ímpar usando o resto da divisão por 2. Se for 0 é par, senão é ímpar.
    print('O número {} é par.'.format(num))
else:
    print('O número {} é ímpar.'.format(num))
