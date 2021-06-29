# Programa que "cadastra" várias pessoas com idade e sexo até o usuário não quiser mais.
# Ao final deverá informar: Quantas pessoas tem mais de 18 anos; quantos homens foram casatrados;
# quantas mulheres com menos de 20 anos.

cpessoas18 = chomens = cmulher20 = 0

while True:
    idade = int(input('Digite a idade da pessoa: '))
    while True:
        sexo = str(input('Digite o sexo da pessoa [M/F]: ')).strip().upper()[0]
        if sexo in 'MF':
            break
        #end-if
    #end-while
    if idade > 18:
        cpessoas18 = cpessoas18 + 1
    if sexo == 'M':
        chomens = chomens + 1
    else:
        if idade < 20:
            cmulher20 = cmulher20 + 1
        #end-if
    #end-if-else
    while True:
        escolha = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
        if escolha in 'SN':
            break
        # end-if
    # end-while
    if escolha == 'N':
        break
    #end-if
#end-while
print(f'O número de pessoas com mais de 18 anos é: {cpessoas18}.')
print(f'O número de homens cadastrados é {chomens}.')
print(f'O número de mulheres com menos de 20 anos é {cmulher20}.')
