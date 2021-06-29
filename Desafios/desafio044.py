# Calcula o valor de um produto conforme a forma de pagamento:
# À vista e em dinheiro: desconto de 10%;
# À vista no cartão: Desconto de 5%;
# Dividir em até 2x no cartão: Preço Normal;
# Dividir em mais de 2x: Juros de 20%.

precoinicial = float(input('Digite o valor do produto: '))
print('Formas de pagmento: ')
print('[ 1 ] - À vista / Dinheiro;')
print('[ 2 ] - À vista / Cartão;')
print('[ 3 ] - Até 2x / Cartão;')
print('[ 4 ] - Mais de 2x / Cartão')
formapagamento = str(input('Escolha (1-4):'))

if formapagamento == '1':
    precofinal = precoinicial - (precoinicial * 10/100)
elif formapagamento == '2':
    precofinal = precoinicial - (precoinicial * 5/100)
elif formapagamento == '3':
    precofinal = precoinicial
elif formapagamento == '4':
    nparcelas = int(input('Qual a quantidade de parcelas? '))
    precofinal = precoinicial + (precoinicial * 20/100)
    print('O produto de R$ {} sairá em {} parcelas de R$ {:.2f}.'.format(precoinicial, nparcelas, precofinal/nparcelas))
# end-elif
else:
    precofinal = 0
    print('Opção errada! Tente de 1 a 4!')
# end-else
print('O valor final para essa forma de pagamento é: R$ {:.2f}'.format(precofinal))
