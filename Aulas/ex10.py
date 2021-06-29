nome = str(input('Digite o seu nome: '))
if nome == 'Gustavo':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal...')
print('Prazer em te conhecer, {}.'.format(nome))
#
#
n1=(float(input('Digite a primeira nota: ')))
n2=float(input('Digite a segunda nota: '))
media = (n1+n2)/2
print('A sua média é {:.1f}.'.format(media))
if media >= 6:
    print('Sua média foi boa!')
else:
    print('Sua média foi ruim!')
#print('Sua média foi boa!' if media >= 6 else 'Sua média foi ruim!')
