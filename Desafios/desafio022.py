#Faz diversas operações com string.

nome = str(input('Digite o nome completo da pessoa: '))
nome.strip() #Elimina os espaços em branco antes, depois e no meio das palavras.
nomecadeia = nome.split()  #Separa o nome em partes [] que serão itens de uma lista [].
print('O nome completo em caixa alta fica: {}'.format(nome.upper()))
print('O nome completo em caixa baixa fica: {}'.format(nome.lower()))
print('O nome completo possui {} caracteres.'.format((len(nome) - nome.count(' '))))
# "Nome" possui o nome completo como originalmente digitado, com espaços. Esse cálculo conta o nome
# forma e subtraí o número de espaços em branco.
print('O primeiro nome é {} e possui {} letras'.format(nomecadeia[0], len(nomecadeia[0])))
