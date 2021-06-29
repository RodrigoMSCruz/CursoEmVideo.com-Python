# Programa lê um número de 00 a 20 e responde mostrando a forma extensa dele usando uma tupla.

extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
           'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    while True:
        num = int(input('Digite um número inteiro entre 00 e 20: '))
        if 0 <= num <= 20:
            break
        # end-if
        else:
            print('Erro! Digite um valor entre 0 e 20.')
        # end-else
    # end-while
    print(f'{num} por extenso é {extenso[num]}.')
    while True:
        continuar = str(input('Deseja continuar: [S/N] ')).strip().upper()[0]
        if continuar in 'SN':
            break
        # end-if
        else:
            print('Erro! Digite S para sim ou N para não.')
        # end-else
    # end-while
    if continuar == "N":
        break
    # end-if
# end-While
