# Escreve os 10 primeiros termos de uma PA(Progresão Aritmétrica) dado o
# primeiro termo e a razão.

primeiro = int(input('Digite o primeiro termo da PA(Progressão Aritmétrica): '))
r = int(input('Digite o valor da razão da PA(Progressão Aritmétrica): '))
ultimo = primeiro + (10 - 1) * r

for i in range(primeiro, ultimo + r, r):
    print('{} -> '.format(i), end =' ')
print('Fim.')
