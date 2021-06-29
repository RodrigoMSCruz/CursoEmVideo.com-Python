# Exibe o primeiro e último nome do nome completo inserido pelo usuário.

nome = str(input('Digite seu nome completo: '))
nome.strip()
nomecadeia = nome.split()
print('O seu primeiro nome é: {}'.format(nomecadeia[0]))
print('O seu último nome é: {}'.format(nomecadeia[len(nomecadeia)-1]))

