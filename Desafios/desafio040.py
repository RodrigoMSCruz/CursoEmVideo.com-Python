# Lê as 2 notas de um aluno e calcula a média do mesmo.
# e diz se foi aprovado, reprovado ou de recuperação.
# Média abaixo de 5, reprovado;
# Média entre 5.0 e 6.9, recuperação;
# Média 7.0 ou superior, aprovado.

nota1 = float(input('Digite a 1ª nota: '))
nota2 = float(input('Digite a 2ª nota: '))
media = (nota1 + nota2) / 2
print('Sua média é: {:.1f}.'.format(media))

if media < 5.0:
    print('Você está REPROVADO!')
#  end-if
elif media >= 5.0 and media < 7.0:
    print('Você está em RECUPERAÇÃO!')
#  end-elif
else:
    print('Parabéns! Você foi APROVADO!')
#  end-else
