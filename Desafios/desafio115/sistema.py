from desafio115.lib.interface import *
from desafio115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar novas pessoas', 'Sair do sistema'])
    if resposta == 1:
        # Opção de ler o arquivo
        lerArquivo(arq)

    elif resposta == 2:
        # Opção de cadastrar pessoa.
        cabecalho('Novo Cadastro')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do sistema... Até mais!')
        sleep(2)
        break
    else:
        cabecalho('Erro! Digite uma opção válida!')
        sleep(2)
    #end-if-elif-else
#end-while