# Melhoria do desafio061 com o adiconal de perguntar continuamente quantos termos a mais uqer ver
# da PA até ser digitado 0.

primeiro = int(input('Digite o primeiro termo da PA(Progressão Aritmétrica): '))
razao = int(input('Digite o valor da razão da PA(Progressão Aritmétrica): '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end=' ')
        termo = termo + razao
        cont = cont + 1
    print('Fim.')
    mais = int(input('Quantos termos a mais você deseja? '))
print('Fim. Foram gerados {} termos ao total.'.format(total))
