# Imprime o somatório de todos os números ímpares e múltplos de 3 no intervalo (1-500).
# (Trechos do código comentado é mais eficiente.)

print('Somatório de todos os números ímpares e múltiplos de 3 no intervalo de 1 a 500:')
s = 0
c = 0

for i in range(1, 501, 1):
#for i in range(1, 501, 2):
    if (i % 2 != 0) and (i % 3 == 0):
#   if (i % 3 ==0):
        s = s + i
        c = c + 1  # c += 1
print('O resultado da soma de {} números é: {}'.format(c,s))