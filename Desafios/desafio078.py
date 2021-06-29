# Programa que leia 5 valores numéricos e guarda-os em uma lista. No final, mostra qual foi o
# maior e o menor valor digitados e as suas respectivas posições na lista.

valores = []
menor = maior = 0

for i in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {i}: ')))
    if i == 0:
        menor = maior = valores[i]
    else:
        if valores[i] < menor:
            menor = valores[i]
        elif valores[i] > maior:
            maior = valores[i]
        # end-if-elif
    # end-if-else
# end-for

print(f'Os valores digitados foram: {valores}.')
print(f'E o menor valor é {menor} nas posições: ', end='')
for p, v in enumerate(valores):
    if v == menor:
        print(f'{p}...', end='')
    # end-if
# end-for
print()

print(f'e o maior é {maior} nas posições: ', end='')
for p, v in enumerate(valores):
    if v == maior:
        print(f'{p}..', end='')
    # end-if
# end-for
print()
