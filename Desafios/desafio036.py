# Programa aprova ou não empréstimo ao usuário.
# Usuário entra com valor da casa, salário do usuário e prazo de pagamento.
# Prestação não deve ultrapassar 30% do salário do usuário.

valorimovel = float(input('Digite o valor da casa a ser financiada: R$ '))
salario = float(input('Digite o valor do seu salário: R$ '))
tempo = (float(input('Digite o tempo de financiamento em anos: ')))

prestacao = valorimovel / (tempo * 12)

if prestacao > (salario * (30 / 100)):
    print('Empréstimo não aprovado. A prestação mensal é superior aos 30% de seu salário.')
else:
    print('Empréstimo aprovado! O valor da sua prestação mensal é inferior ou igual a 30% de seu salário.')

print('30% de seu salário equivale a R$ {:.2f} e o valor da prestação é R$ {:.2f}.'.format((salario * 0.3), prestacao))
