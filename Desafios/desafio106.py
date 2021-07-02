# Mini-sistema que utiliza o Interactive Help do Python. O usuário vai digitar o comando e o manual vai
# aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.

from time import sleep

def ajuda(com):
    sleep(1)
    help(com)
# end-def-ajuda


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print('˜' * tam)
    print(f' {msg}')
    print('˜' * tam)
# end-def-titulo

comando = ''
while True:
    titulo('SISTEMA DE AJUDA PYHELP')
    comando = str(input('Digite a Função ou Bibioteca [FIM p/ encerrar]: '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
    # end-if-else
# end-while
sleep(2)
print('Encerrando... Até breve.')
