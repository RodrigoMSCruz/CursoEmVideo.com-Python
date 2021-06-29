# Programa que simula o saque de um caixa eletrônico.
# Deve informar quantas notas de R$ 50, R$ 20, R$ 10 e R$ 1 serão entregues conforme o valor solicitado.

# n50 = n20 = n10 = n1 = resto = 0

valor = int(input('Informe o valor do saque (Disponíveis apenas notas de R$ 1, 10, 20 e 50): R$ '))
n50 = valor // 50
resto = valor % 50
n20 = resto // 20
resto = resto % 20
n10 = resto // 10
resto = resto % 10
n1 = resto // 1

print(f'O saque de R$ {valor} será entregue em:')
if n50 > 0:
    print(f'{n50} notas de R$ 50.')
if n20 > 0:
    print(f'{n20} notas de R$ 20.')
if n10 > 0:
    print(f'{n10} notas de R$ 10.')
if n1 > 0:
    print(f'{n1} notas de R$ 1.')
