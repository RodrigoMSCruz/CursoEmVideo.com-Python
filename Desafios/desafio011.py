# Calcula a quantidade de tinta em l para pintar uma parede dado a altura e largura da mesma para cálculo da área.
# 1 litro de tinta pinta 2m2(2 metros quadrados) de área.
altura = float(input('Digite a altura da área a ser pintada(m): '))
largura = float(input('Digite a largura da área a ser pintada(m): '))
area = altura * largura
qtintalitro = area / 2
print('A área informada é de {}m2.\nSão necessários {}l de tinta para pintá-la.'.format(area, qtintalitro))
