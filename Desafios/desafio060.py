# Programa que calcula o fatorial de um número inserido pelo usuário.

n = int(input('Digite o valor a ser calculado o fatorial: '))

i = n
fat = 1
while i != 0:
    fat = fat * i
    i = i - 1
# end-while
print('Resultado do fatorial de {} com while: {}.'.format(n, fat))

# Mesmo exercício, apenas usando a estrutura FOR.
fat = 1
for i in range(n, 0, -1):
    fat = fat * i
# end-for
print('Resultado do fatorial de {} com for: {}.'.format(n, fat))
