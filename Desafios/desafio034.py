# Pede a inserção do salário do usuário. Funcionários com salários superiores a R$ 1250,00
# recebem aumento de 10%. Salários inferiors a R$ 1250,00 recebem aumento de 15%.

salario = float(input('Digite o valor do seu salário: R$ '))
if salario > 1250.00:
    aumento = salario + (salario * 0.10)  # * 10/100
else:
    aumento = salario + (salario * 0.15)  # * 15/100
print('Seu novo salário é de R$ {:.2f}.'.format(aumento))
