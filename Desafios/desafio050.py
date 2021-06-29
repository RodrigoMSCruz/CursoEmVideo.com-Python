# Lê 6 números e mostra o somatório deles. Se for digitado um valor
# ímpar, é desconsiderado.

print('Digite 6 números para serem somados. Números ímpares serão desconsiderados.')
s = 0
c = 0

for i in range (1, 7, 1):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        s = s + n # s =+ n
        c = c + 1 # c += 1
print('O somatório de {} números pares é: {}.'.format(c, s))