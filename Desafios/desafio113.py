# Reescrita da função leiaInt() feita no desafio 104, incluindo agora a possibilidade da digitação
# de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaInt(msg):
    while True:
        try:
            n = str(input(msg))
            valor = int(n)
        except (ValueError, TypeError):
            print('\033[0;31mErro! Digite um valor válido.\033[m')
            continue
        except (KeyboardInterrupteyboardInterrupt):
            print('\033[0;31mPrograma encerrado pelo usuário.\033[m')
            return 0
        else:
            return valor
        #end-try-except-else
    #end-while
#end-def


def leiaFloat(msg):
    while True:
        try:
            n = str(input(msg))
            valor = float(n)
            ok = True
        except (ValueError, TypeError):
            print('\033[0;31mErro! Digite um valor válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[0;31mPrograma encerrado pelo usuário.\033[m')
            return 0
        else:
            return valor
        #end-try
    #end-while
#end-def

ni = leiaInt('Digite um número inteiro: ')
nf = leiaFloat('Digite um número real: ')
print(f'Você acabou de digitar o número inteiro {ni} e um número real {nf}.')