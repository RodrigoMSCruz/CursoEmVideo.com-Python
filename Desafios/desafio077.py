# Programa com uma TUPLA com várias palavras (sem acentos). Depois disso, deve mostrar,
# para cada palavra, quais são as suas vogais.

print('Digite 7 palavras para serem analisadas:')
p1 = str(input('Digite a primeira palavra: '))
p2 = str(input('Digite a segunda palavra: '))
p3 = str(input('Digite a terceira palavra: '))
p4 = str(input('Digite a quarta palavra: '))
p5 = str(input('Digite a quinta palavra: '))
p6 = str(input('Digite a sexta palavra: '))
p7 = str(input('Digite a sétima palavra: '))
palavras = (p1, p2, p3, p4, p5, p6, p7)

# palavras = ('Casa', 'Predio', 'Python', 'Computador', 'Internet', 'Celular', 'Programador')

for p in palavras:
    print(f'\nPalavra {p.upper()}, temos as vogais: ', end='')
    for l in p:
        if l.upper() in 'AEIOU':
            print(l.upper(), end='')
        # end-if
    # end-for
# end-for
