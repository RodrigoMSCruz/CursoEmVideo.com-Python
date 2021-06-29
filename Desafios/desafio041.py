# Lê o ano de nascimento do atleta e o classifica conforme a idade nas seguintes categorias:
# Abaixo de 9 anos: Mirim
# Até 14 anos: Infantil;
# Até 19 anos: Júnior
# Até 25 aos: Sênior;
# acima de 25: Master.

from datetime import date

anonasc = int(input('Digite o ano de nascimento do atleta: '))
idade = date.today().year - anonasc

if idade <= 9:
    print('Categoria MIRIM.')
elif idade <= 14:
    print('categoria INFANTIL.')
elif idade <= 19:
    print('Categoria: JÚNIOR.')
elif idade <= 25:
    print('Categoria: SÊNIOR.')
else:
    print('Categoria: MASTER.')
#  end-if-elif-else