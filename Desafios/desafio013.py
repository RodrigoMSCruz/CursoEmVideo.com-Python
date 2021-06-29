# Calcula o aumento de 15% de aumento no salário inserido pelo usuário.
sal = float(input('Digite o valor de seu salário (R$): '))
novosal = sal + (sal * 0.15)
#novosal = sal + (sal * (15/100))
print('O seu salário de R$ {:.2f} com 15% fica com o valor de {:.2f}'.format(sal,novosal))
