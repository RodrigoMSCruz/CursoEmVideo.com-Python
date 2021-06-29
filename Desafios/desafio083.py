# Programa onde o usuário digite uma expressão qualquer que use parênteses. A aplicação deve
# analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

abre = fecha = 0
expressao = str(input('Digite a expressão a ser analisada: '))

for c in expressao:
    if c == '(':
        abre = abre = 1
    elif c == ')':
        fecha = fecha + 1
    # end-if-elif
# end-for
if abre == fecha:
    print('A expressão está OK!')
else:
    print('A expressão está errada!')
# end-if