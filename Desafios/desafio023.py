# Lê um número de 4 dígitos e o divide em unidades, dezenas, centenas e milhares.

# num = str(input('Digite um número entre 0 e 9999: '))
# t= int(len(num))
# print('Unidade: {}'.format(num[t-1]))
# print('Dezena: {}'.format(num[t-2]))
# print('Centena: {}'.format(num[t-3]))
# print('Milhar: {}'.format(num[t-4]))
num = int(input('Digite um número entre 0 e 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
