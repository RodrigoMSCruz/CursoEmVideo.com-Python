# Programa com uma função chamada escreva(), que recebe um texto qualquer como parâmetro e mostra
# uma mensagem com tamanho adaptável.

def escreva(txt):
    comprimento = len(txt) + 4
    print('˜' * comprimento)
    print(f'  {txt}')
    print('˜' * comprimento)
# end-defEscreva


escreva('Olá, mundo!')
escreva('Curso de Python no YouTube')
escreva('CeV')
