# Programa que lê vários números inteiros pelo teclado. No final da execução, mostre a média
# entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao
# usuário se ele quer ou não continuar a digitar valores.

continuar = 'S'
soma = menor = maior = cont = 0

while continuar == 'S':
    n = int(input('Digite um número inteiro: '))
    soma = soma + n
    cont = cont + 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    continuar = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0] #Pegar apenas a primeira letra da resposta e em caixa alta.
#end-while
print('A média de valores digitado é: {}'.format(soma/cont))
print('O maior valor digitado foi {} e o menor é {}.'.format(maior, menor))