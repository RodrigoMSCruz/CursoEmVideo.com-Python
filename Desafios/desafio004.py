algo = input('Digite algo para ser analisado: ')
print('O tipo primitivo é {}'. format(type(algo)))
print('É númerico: {}.'.format(algo.isnumeric()))
print('É alfabético: {}.'.format(algo.isalpha()))
print('Só tem espaços: {}.'.format(algo.isspace()))
print('É caixa alta: {}.'.format(algo.isupper()))
print('É caixa baixa: {}. '.format(algo.islower()))
print('É capitular: {}.'.format(algo.istitle()))