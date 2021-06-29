numeros = [[], []]

for i in range(1, 8, 1):
    valor = int(input(f'Digite o {i}º número: '))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)
    # end-if
# end-for
numeros[0].sort()
numeros[1].sort()
print(f'Os números pares são: {numeros[0]}')
print(f'Os números ímpares são: {numeros[1]}')
