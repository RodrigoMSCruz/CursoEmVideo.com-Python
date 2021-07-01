# Programa com a função leiaInt(), que funciona de forma semelhante ‘a função input() do Python, só que
# fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

def leiaint(msg):
    ok = False
    valor = 0
    while True:
        num = str(input(msg))
        if num.isnumeric():
            valor = int(num)
            ok = True
        else:
            print('\033[0;31mErro! Digite um valor válido.\033[m')
        # end-if-else
        if ok:
            break
        # end-if
    # end-while
    return valor
# end-def-leiaInt


# Programa Principal
n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
