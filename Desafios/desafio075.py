# Programa que lê 4 valores pelo teclado e guarda-os em uma TUPLA(). No final, mostre:
# Quantas vezes apareceu o valor 9;
# Em que posição foi digitado o 1º valor 3;
# Quais foram os números pares.

n1 = int(input('Digite um valor inteiro: '))
n2 = int(input('Digite um valor inteiro: '))
n3 = int(input('Digite um valor inteiro: '))
n4 = int(input('Digite um valor inteiro: '))
valores = (n1, n2, n3, n4)

print('=-'*25)
print(f'O número 9 apareceu {valores.count(9)} vezes.')
if 3 in valores:
    print(f'O primeiro número 3 está na posição {valores.index(3)+1}.')
else:
    print('O número 3 não foi digitado.')

print('O números pares são: ', end='')
for i in valores:
    if i % 2 == 0:
        print(f'{i}', end=' ')
    # end-if
# end-for
print('\n', '=-'*25)
