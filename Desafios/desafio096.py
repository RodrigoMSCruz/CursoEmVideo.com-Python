# Programa com uma função chamada área(), que recebe as dimensões de um terreno retangular
# (largura e comprimento) e mostra a área do terreno.

def area(l, h):
    a = l * h
    print(f'A área de um terreno {l:2.2f} x {h:2.2f} é de {a:2.2f}m2.')
# end-defArea


print('Controle de Terrenos')
print('-' * 20)
a = float(input('LARGURA (m): '))
b = float(input('COMPRIMENTO (m): '))
area(a, b)
