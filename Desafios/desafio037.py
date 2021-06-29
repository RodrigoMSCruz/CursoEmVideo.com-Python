# Lê um número inserido pelo usuário e o converte para binário, octal ou hexadecimal.

n = int(input('Digite um valor inteiro a ser convertido: '))

print('Escolha a base de conversão: ')
print('[ 1 ] - Binário;')
print('[ 2 ] - Octal;')
print('[ 3 ] - Hexadecimal.')
escolha = int(input('Escolha: '))

if escolha == 1:
    resultado = bin(n)
elif escolha == 2:
    resultado = oct(n)
elif escolha == 3:
    resultado = hex(n)
else:
    resultado = '  NULO! Opção não existente nessa versão.'
    # Há 2 caracteres em branco no começo da mensagem propositalmente por causa da linha abaixo.
print('O resultado é : {}.'.format(resultado[2:]))  # [2:] Faz com que só seja mostrado a string após o 2º caractere.
