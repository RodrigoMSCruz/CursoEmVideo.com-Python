# programa lê o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# a média de idade do grupo;
# qual é o nome do homem mais velho;
# quantas mulheres têm menos de 20 anos.

nome_l = ['', '', '', '']
idade_l = [0,0,0,0]
sexo_l = ['', '', '', '']

for i in range(0, 4, 1):
    print('=-'*20)
    nome_l[i] = str(input('Digite o nome da {}ª pessoa: '.format(i+1)))
    idade_l[i] = int(input('Digite a idade da {}ª pessoa: '.format(i+1)))
    sexo_l[i] = str(input('Digite o sexo da {}ª pessoa [M/F]: '.format(i+1))).upper()
# end-for

# Cálculo e exibição da média de idade do grupo:

media_idade = 0
for i in range(0,4,1):
    media_idade = media_idade + idade_l[i]
# end-for
media_idade = media_idade / 4

print('=-'*30)
print('')
print('=-'*30)
print('A média de idade do grupo é de {} anos.'.format(media_idade))

# Cálculo do nome do homem mais velho do grupo:

i_maisvelho = -1
for i in range(0,4,1):
    if sexo_l[i] == 'M' and idade_l[i] > i_maisvelho:
        i_maisvelho = i
    #end-if
#end-for

print('=-'*30)
print('O homem mais velho do grupo é {} e ele tem {} anos de idade.'.format(nome_l[i_maisvelho], idade_l[i_maisvelho]))

# Cálculo de quantas mulheres têm menos de 20 anos:

qmulher20 = 0
for i in range(0, 4, 1):
    if sexo_l[i] == 'F' and idade_l[i] < 20:
        qmulher20 = qmulher20 + 1
    # end-if
#end-for

print('=-'*30)
print('O número de mulheres com menos de 20 anos do grupo é: {}.'.format(qmulher20))
