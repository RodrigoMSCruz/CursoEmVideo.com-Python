# Programa que usa uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função
# vai sortear 5 números e vai colocá-los dentro da lista e a segunda função mostra a soma entre todos os valores
# pares sorteados pela função anterior.

from random import randint
numerossorteados = []

def sorteia(numerossorteados):
    print(f'Sorteando 5 valores na lista: ', end='')
    for i in range(0, 5, 1):
        numerossorteados.append(randint(1, 10))
        print(f'{numerossorteados[i]} ', end='')
    #end-if
    print('PRONTO!')
#end-def

def somapar(numerossorteados):
    soma = 0
    for i in numerossorteados:
        if i % 2 == 0:
            soma = soma + i
        #end-if
    #end-for
    print(f'O resultado da soma dos pares é: {soma}')
#end-def

sorteia(numerossorteados)
somapar(numerossorteados)