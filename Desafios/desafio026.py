# Lê uma frase inserida pelo usuário e mostra quantas vezes a letra "A"aparece, e em que posição
# aparece a primeira ocorrência e a última.

frase = str(input('Digite uma frase: '))
frase.strip()
frase = frase.upper()
print('A letra "A" apareceu {} vezes.'.format(frase.count('A')))
print('A primeira letra "A" aparece na posição: {}'.format(frase.find('A')+1))  # Procura da esquerda para a direita.
print('A última letra "A" aparece na posição : {}'.format(frase.rfind('A')+1))  # Procura da direita para a esquerda.

