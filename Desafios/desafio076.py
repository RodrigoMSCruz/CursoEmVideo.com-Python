# Programa com uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostra uma listagem de preços, organizando os dados em forma tabular.

produto = ('Mouse', 50.0, 'HD Externo', 420.0, 'Smartphone', 1300.0, 'Memória 4 GB', 290.40)

print('-'*30)
print('Listagem de Preços')
print('-'*30)

for i in range(0, len(produto), 2):
    print(f'{produto[i]:<.30} R${produto[i+1]:>5.2f}')

print('-'*30)
