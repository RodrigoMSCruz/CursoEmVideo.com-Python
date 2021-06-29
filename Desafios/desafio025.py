# Checa se o nome inserido pelo usuário possui "Silva" em qualquer parte do nome.

nomecompleto = str(input('Digite seu nome completo: '))
nomecompleto.strip()
print('Possui Silva: {}'.format('SILVA' in nomecompleto.upper()))
