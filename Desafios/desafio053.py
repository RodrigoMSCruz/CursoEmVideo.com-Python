# Programa que lê uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# Exemplos de palíndromos:
# APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

frasedigitada = str(input('Digite a frase a ser analisada: ')).strip()
aux = frasedigitada.split()
frasefinal = ''.join(aux)
frasefinal = frasefinal.upper()
frasereversa = ''

for i in range(len(frasefinal) -1, -1, -1):
    frasereversa = frasereversa + frasefinal[i]

print('Você digitou: {}'.format(frasedigitada))
print('A frase sem espaços e em caixa alta fica: {}'.format(frasefinal))
print('E ela invertida fica: {}'.format(frasereversa))

if frasefinal == frasereversa:
    print('A frase é um PALÍNDROMO.')
else:
    print('A frase NÃO é um palíndromo.')
