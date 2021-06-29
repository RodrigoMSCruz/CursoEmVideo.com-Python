from desafio115.lib.interface import *


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
#end-def


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close
    except:
        print('Erro com arquivo')
    else:
        print('Arquivo criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo.')
    else:
        cabecalho('PESSOAS CADASTRADAS:')
        for linha in a:
            dado = linha.split(';')
            dado[1]=dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:3}')
        #end-for
    finally:
        a.close()
    #end-try-except-else-finally
#end-def


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Erro! Houve uma falha com a abertura do arquivo.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na gravação desse registro.')
        else:
            print(f'Registro de {nome} concluído com sucesso!')
        #end-try-except-else
    #end-try-except-else
#end-def