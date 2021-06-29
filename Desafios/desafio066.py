# Programa que lê vários inteiros digitados pelo usuário até ele digitar 999.
# Ao digitar 999, ele mostra quantos números foram digitados e a soma entre eles.

cont = soma = 0
n = int(input('Digite um valor inteiro. [Digite 999 para parar]: '))

while n != 999:
    cont = cont + 1
    soma = soma + n
    n = int(input('Digite um valor inteiro. [Digite 999 para parar]: '))
# end-while
print(f'Total de números: {cont} - Somatório: {soma}')

# Usando Break

#while True:
#    n = int(input('Digite um valor inteiro. [Digite 999 para parar]: '))
#    if n == 999:
#        break
#    cont = cont + 1
#    soma = soma + n
#print(f'Total de números: {cont} - Somatório: {soma}')