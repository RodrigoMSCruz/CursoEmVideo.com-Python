# Programa que lê o nome e duas notas de vários alunos e guarda tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas
# de cada aluno individualmente.

boletim = []
cont = 0

while True:
    nome = str(input('Digite o nome do aluno: '))
    nota1 = float(input('Digite a 1ª nota do aluno: '))
    nota2 = float(input('Digite a 2ª nota do aluno: '))
    media = (nota1 + nota2) / 2
    boletim.append([nome, [nota1, nota2], media])
    while True:
        continuar = str(input('Deseja continuar? (S/N)? ')).strip().upper()[0]
        if continuar in 'SN':
            break
        else:
            print('Digite S para sim e N para Não.')
        # end-if-else
    # end-while
    if continuar == 'N':
        break
    # end-if
# end while
print('-=-=-=-=-=BOLETIM-=-=-=-=-=')
print(f'{"Nº":<4}{"Nome":<10}{"Media":>8}')
for i, a in enumerate(boletim):
    print(f'{i}                   {a[0]}                        {a[2]}')
# end for
while True:
    escolha=int(input('Escolha o aluno que deseja ver as notas. 999 para sair: '))
    if escolha == 999:
        print('Fechando o programa. Até mais!')
        break
    else:
        print(f'Aluno(a): {boletim[escolha][0]} - Nota 1: {boletim[escolha][1][0]} - Nota 2: {boletim[escolha][1][1]}')
    # end-if-else
# end-while
