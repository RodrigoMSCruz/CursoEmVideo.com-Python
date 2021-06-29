# Mostra os n primeiros termos da sequência de Fibonacci, sendo o valor n digitado pelo usuário.

n = int(input('Digite quantos valores da seqência de Fibonacci deseja [3 ou mais]: '))
ant1 = 1
ant2 = 0
prox = 0
c = 2 # Os valores 0 e 1 já ão existentes antes do lagoritmo de Fibonacci funcionar.
print('0 -> 1 -> ', end ='')

while c < n:
    prox = ant1 + ant2
    print('{} -> '.format(prox), end='')
    ant2 = ant1
    ant1 = prox
    c = c + 1
print('Fim.')
