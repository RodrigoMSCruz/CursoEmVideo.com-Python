def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg))
        entrada.replace(',', '.').strip()
        if entrada.isalpha() or entrada.strip() == '':
            print(f'ERRO! {entrada} é um preço inválido!')
        else:
            valido = True
            return float(entrada)
        # end-if-else
    # end-while
# end-def-leiadinheiro
