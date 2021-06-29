# Programa onde o usuário possa digitar cinco valores numéricos e cadastrá-los em uma
# lista, já na posição correta de inserção (sem usar o sort()). No final, mostra a lista
# ordenada na tela.

valores = []

for i in range(0, 5, 1):
    valor = int(input('Digite um valor: '))
    if len(valores) == 0:  # Quando a lista está vazia, o primeiro valor simplesmente é adicionado.
        valores.append(valor)
        print(f'O número {valor} é o primeiro número. Posição 0.')
    elif valor < valores[0]:  # Quando o valor digitado é menor que o primeiro, é inserido no começo da lista, na posiçào 0.
        valores.insert(0, valor)
        print(f'O número {valor} foi inserido no começo, na posição 0')
    elif valor > valores[len(valores) - 1]:  # Quando o valor é maior que o último da lista, é inserido no final.
        valores.append(valor)
        print(f'O número {valor} foi inserido no final, na posição {len(valores) - 1}.')
    else:  # Quando está entre o primeiro e o último, varre a lista toda até achar algum valor maior que ele e insere no seu lugar.
        posicao = 0
        while posicao < len(valores):
            if valor <= valores[posicao]:
                valores.insert(posicao, valor)
                print(f'O número {valor} foi inserido na posição {posicao}.')
                break
            # end-if
            posicao = posicao + 1
        # end-while
    # end-if-elif-else
# end-for

print(valores)
