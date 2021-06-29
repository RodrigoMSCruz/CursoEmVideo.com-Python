# Escreve os 10 primeiros termos de uma PA(Progresão Aritmétrica) dado o
# primeiro termo e a razão.
# Baseado no desafio051, mas em vez de usar estrutura "For", usar com "While".

primeiro = int(input('Digite o primeiro termo da PA(Progressão Aritmétrica): '))
r = int(input('Digite o valor da razão da PA(Progressão Aritmétrica): '))
i = primeiro
ultimo = primeiro + (10 - 1) * r

while i != (ultimo + r):
    print('{} -> '.format(i), end=' ')
    i = i + r
print('Fim.')

# Código abaixo comentado faz o mesmo que o acima, porém, com "For", como no programa original desafio051.
#for i in range(primeiro, ultimo + r, r):
#    print('{} -> '.format(i), end =' ')
#print('Fim.')