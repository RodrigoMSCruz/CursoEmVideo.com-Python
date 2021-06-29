# Programa que lê o nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostra o conteúdo da estrutura na tela.

aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] >= 7.0:
    aluno['situacao'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'

for k, v in aluno.items():
    print(f'O(a) {k} é igual {v}.')
