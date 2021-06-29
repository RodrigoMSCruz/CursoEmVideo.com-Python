# Aprimoramento do desafio anterior, mostrando no final:
# A soma de todos os valores pares digitados; A soma dos valores da terceira coluna; O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

#           [0] [0] [0]
# matriz =  [0] [0] [0]
#           [0] [0] [0]

somapar = somacol3 = maiorlin3 = 0

for y in range(0, 3):
    for x in range(0, 3):
        n = int(input(f'Digite o valor para a posição [{y , x}]: '))
        matriz[y][x] = n
    # end-for
# end-for
for y in range(0, 3):
    print(matriz[y])
# end-for
for y in range(0, 3):
    for x in range(0, 3):
        if matriz[y][x] % 2 == 0:
            somapar = somapar + matriz[y][x]
        # end-if
    # end-for
# end-for
print(f'A soma de todos os pares é: {somapar}.')

for y in range(0, 3):
    somacol3 = somacol3 + matriz[y][2]
# end-if
print(f'A soma de todos da 3ª coluna é: {somacol3}.')

for x in range(0, 3):
    if x == 0:
        maiorlin3 = matriz[2][x]
    else:
        if matriz[2][x] > maiorlin3:
            maiorlin3 = matriz[2][x]
        # end-if
    # end-if-else
# end-for
print(f'O maior valor da 2ª linha é {maiorlin3}.')
