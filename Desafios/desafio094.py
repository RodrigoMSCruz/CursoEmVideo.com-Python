# Programa que lê nome, sexo e idade de várias pessoas, guardando os dado de cada pessoa em um
# dicionário e todos os dicionários em uma lista. No final, mostra:
# Quantas pessoas foram cadastradas; A média de idade; Uma lista com as mulheres; Uma lista de pessoas com idade acima
# da média.

cadastro = []
pessoa = {}
somaidade = mediaidade = 0

while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Inválido! Digite apenas M ou F.')
    # end-while
    pessoa['idade'] = int(input('Idade: '))
    somaidade = somaidade + pessoa['idade']
    cadastro.append(pessoa.copy)
    continua = str(input('Deseja cadastrar mais? [N para Não.]: ')).upper()[0]
    if continua == 'N':
        break
    # end-if
# end-while

print(f'Foram cadastradas {len(cadastro)} pessoas.')

mediaidade = somaidade / len(cadastro)
print(f'A média de idade é {mediaidade:5.2f} anos.')

print('Lista das mulheres cadastradas:')
for cad in cadastro:
    if cad['sexo'] == 'F':
        print(f'{cad["nome"]}')
    # end-if
# end-for
print()

print('Lista das pessoas acima da média de idade:')
for cad in cadastro:
    if cad['idade'] > mediaidade:
        print(f'{cad["nome"]}')
    # end-if
# end-for
