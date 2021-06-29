# Programa que lê dois valores e mostre um menu na tela:
#[ 1 ] somar; [ 2 ] multiplicar;[ 3 ] maior;[ 4 ] novos números e[ 5 ] sair do programa.
# O programa realiza a operação solicitada em cada caso.

resultado = 0
escolha = 0

n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))

while escolha != 5:
    print('=-'*10)
    print('MENU DE OPÇÕES')
    print('[ 1 ] - Somar;')
    print('[ 2 ] - Multiplicar;')
    print('[ 3 ] - Maior Valor;')
    print('[ 4 ] - Novos Números.')
    print('[ 5 ] - Sair.')
    print('=-' * 10)
    escolha = int(input('Escolha [1-5]: ' ))

    if escolha == 1:
        resultado = n1 + n2
        print('Resultado da soma é {}.'.format(resultado))
    elif escolha ==2:
        resultado = (n1 * n2)
        print('O resultado da multiplicação é {}.'.format(resultado))
    elif escolha == 3:
        if n1 > n2:
            resultado = str(n1)
            print('O maior é {}.'.format(resultado))
        elif n2 > n1:
            resultado = str(n2)
            print('O maior é {}.'.format(resultado))
        elif n1 == n2:
            resultado = 'Os 2 números são iguais.'
            print(resultado)
        #end elif
    elif escolha == 4:
        print('Informe os números novamente:')
        n1 = int(input('Digite o 1º número: '))
        n2 = int(input('Digite o 2º número: '))
    elif escolha == 5:
        print('Finalizando.')
    else:
        print('Opção inexistente. Digite novamente.')
    #end if
#end while
