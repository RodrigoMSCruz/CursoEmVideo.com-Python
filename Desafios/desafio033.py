# Pede para o usuário entrar com 3 valores e o programa  informa qual é o menor e o maior deles.

n1 = int(input('Digite um valor inteiro para o primeiro número: '))
n2 = int(input('Digite um valor inteiro para o segundo número: '))
n3 = int(input('Digite um valor inteiro para o terceiro número: '))
seq = [n1, n2, n3]  # Cria uma lista com os valores digitados pelo usuário.
seq.sort()  # Ordena a lista.
print('O menor número é {} e o maior é {}.'.format(seq[0], seq[2]))
# Array de 3: 0-2. A posição começa de 0.
