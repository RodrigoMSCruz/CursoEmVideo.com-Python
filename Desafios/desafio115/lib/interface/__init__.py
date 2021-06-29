def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


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


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c = c + 1
    #end-for
    print(linha())
    opc = leiaInt('Sua Opção: ')
    return opc
#end-def