# Programa que declara uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostra
# a matriz na tela, com a formatação correta.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for y in range(0, 3):
    for x in range(0, 3):
        n = int(input(f'Digite o valor para a posição [{y , x}]: '))
        matriz[y][x] = n
    # end-for
# end-for
for y in range(0, 3):
    print(matriz[y])
# end-for
