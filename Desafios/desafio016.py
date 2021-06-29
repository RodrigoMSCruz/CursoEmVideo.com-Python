# Arredondar um número digitado pelo usuário e mostrá-lo na tela.
# Usando biblioteca ou com formatação de saída.
from math import trunc

num = float(input('Digite um número real: '))
print('A parte inteira de {} é {}.'.format(num, trunc(num)))
#print('A parte inteira de {} é {:.0f}.'.format(num, num))
