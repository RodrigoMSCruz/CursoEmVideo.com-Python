#  Atualização do desafio035:
#  Além de informar se 3 segmentos de reta podem ou não fazer um triângulo,
#  esse programa adiciona a funcionalidade de informar se é um triangulo
#  equilátero, isóceles ou escaleno.
#  --=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=
#  RELEMBRANDO:
#  Para saber se é um triângulo, cada lado deve ser menor que a soma dos outros 2. -> r1<r2+r3, r2<r1+r3 e r3<r1+r2
#  Triaângulo equlátero: Todos os lados são iguais -> r1=r2=r3
#  Para saber se é um triângulo isocéles, ao menos 2 lados devem ter meso tamanho. -> r1=r2 XOR r2=r3 XOR r3=r1
#  OBSERVAÇÃO: XOR = OU Exclusvo.

r1 = float(input('Digite o cumprimento do segmento de reta 1: '))
r2 = float(input('Digite o cumprimento do segmento de reta 2: '))
r3 = float(input('Digite o cumprimento do segmento de reta 3: '))

if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2:  # Determina se é triangulo
    # Bloco SE FOR TRIÂNGULO
    if r1 == r2 == r3:
        print('Esse é um triângulo equilátero.')
    # end-if
    elif (r1 == r2) ^ (r2 == r3) ^ (r1 == r3):  # ^ = XOR(OU EXCLUSIVO)
        print('Esse é um triângulo isóceles.')  # Verifica se apenas 2 e apenas 2 lados são iguais.
    # end-elif
    else:
        print('Esse é um triângluolo escaleno.')
    # end-else
# end-if
else:  # Se não for triângulo
    print('Essas retas NÃO podem formar um triângulo.')
# end-else
