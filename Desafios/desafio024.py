# Checa se o nome da cidade digitada pelo usuário começa com "Santo".

nomecidade = str(input('Digite o nome da cidade: '))
nomecidade.strip()
nomecidade = nomecidade.upper()
print(nomecidade[0:5] == 'SANTO')