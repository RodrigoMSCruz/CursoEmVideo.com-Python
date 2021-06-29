# Programa mostra a tabuada de qualquer número inserido pelo usuário continuamente até o usúario digitar
# um número negativo, que é a condição de parada(flag).

while True:
    n = int(input('Quer ver a tabuada de qual valor? [Digite negativo para sair]: '))
    if n < 0:
        break
    # end-while
    else:
        for i in range(1,11,1):
            print(f'{n} x {i:2} = {n * i}')
        #end-for
    #end-else
#end-while

print('Programa Tabuada encerrado. Volte sempre!')