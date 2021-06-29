# Programa lê o sexo da pessoa, mas que só aceita "M" o "F".

sexo = str(input('Digite o seu sexo: [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Digite o seu sexo: [M/F]: ')).strip().upper()[0]
# end-while
print('Sexo {} registrado com sucesso'.format(sexo))