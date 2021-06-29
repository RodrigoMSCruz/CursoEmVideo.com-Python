# Programa que lê nome, ano de nascimento e carteira de trabalho e cadastra-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import date

cadastro = {}

cadastro['nome'] = str(input('Digite o nome do trabalhador: '))
anonasc = int(input('Digite o ano de nascimento: '))
cadastro['idade'] = int(date.today().year - anonasc)
cadastro['ctps'] = str(input('Digite a CTPS (0 não tem): '))
if cadastro['ctps'] != '0':
    cadastro['anocontr'] = int(input('Ano da contratação: '))
    cadastro['salario'] = float(input('Digite o salário: R$ '))
    cadastro['aposentadoria'] = cadastro['idade'] + (cadastro['anocontr'] + 35) - date.today().year
# end-for
for k, v in cadastro.items():
    print(f'{k} possui o valor armazenado de: {v}.')
# end-for
