# Programa retorna se um número inserido pelo usuário é primo ou não.
# Um número é definido como primo se for apenas dívisel por 1 e ele mesmo, então, se a quantidade
# de números pelo qual ele 'divísivel for igual a 2, é primo.

n = int(input('Digite um número: '))
cont = 0                        # Contador para os números divisíveis.

for i in range(1, n + 1, 1):      # Laço percorre todos os números de 1 até o número digitado.
    if n % i == 0:              # O número digitado será checado se tem dvisão inteira por todos do laço
        cont = cont +1          # Para cada número que resultar em resto da divisão inteira =0, o contador será acrescido em 1.

if cont == 2:                   # Números primos só são divísiveis por 2 números: 1 e ele mesmo. Se cont=2, então é primo.
    print('{} é primo, pois é divísel por apenas 1 e {}.'.format(n, n))
else:
    print('{} NÃO é primo, pois ele é divisível por {} números.'.format(n, cont))
