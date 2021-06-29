# O programa pede o cumprimento de 3 segmentos de retas e o programa retorna se é possível
# ou não que eles formarem um triângulo.

# REGRA PARA FORMAÇÃO DE UM TRIÂNGULO:
# Cada um dos lados precisa ser menor que a soma dos outros 2 segmentos.

r1 = float(input('Digite o cumprimento do segmento de reta 1: '))
r2 = float(input('Digite o cumprimento do segmento de reta 2: '))
r3 = float(input('Digite o cumprimento do segmento de reta 3: '))

if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2:
    print('Essas retas podem formar um triângulo.')
else:
    print('Essas retas NÃO podem formar um triângulo.')
