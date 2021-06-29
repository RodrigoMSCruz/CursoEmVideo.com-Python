# Programa lê o ano de nascimento do usuário e diz se está na hora de se alistar no
# serviço militar ou não e se não, quanto tempo falta ou já passou.

from datetime import date

anousuario = int(input('Digite o ano de seu nascimento: '))
anoatual = date.today().year
idade = anoatual - anousuario

if idade < 18:
    diferenca18 = 18 - idade
    print('Você ainda irá se alistar. Faltam {} anos para o alistamneto.'.format(diferenca18))
    print('O ano de seu alistamneto será {}.'.format(anoatual + (diferenca18)))
#  end-if
elif idade == 18:
    print('Já é hora de se alistar.')
#  end-elif
else:
    diferenca18 = idade - 18
    print('Já passou do tempo de se alistar! Já passou {} anos.'.format(diferenca18))
    print('O ano que você deveria ter se alistado foi: {}.'.format(anoatual-(diferenca18)))
#  end-else
