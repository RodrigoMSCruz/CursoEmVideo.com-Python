#Programa que Lê um ângulo e exibe o seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians

angulo = float(input('Digite um ângulo: º'))
rad = radians(angulo) #Necessário converter para radianos, pois as funções sin(), cos() e tan() funcionam com radianos.
print('O ângulo {}, em radianos é {} e tem os seguintes valores:'.format(angulo, rad))
print('Seno: {:.2f}, Cos: {:.2f} e Tg: {:.2f}.'.format(sin(rad), cos(rad), tan(rad)))
