# Recebe os nomes de 4 alunos inseridos pelo usuário e o software escolhe aleatoriamente 1 deles.

from random import choice
a1 =str(input('Digite o nome do aluno(a) 1: '))
a2 =str(input('Digite o nome do aluno(a) 2: '))
a3 =str(input('Digite o nome do aluno(a) 3: '))
a4 =str(input('Digite o nome do aluno(a) 4: '))
listaaluno = [a1, a2, a3, a4] #Declaação de uma lista. Isso é mostrado mais à frente no curso de Python do CursoEmVideo.com
escolhido = choice(listaaluno)
print('O aluno(a) escolhido(a) é: {}'.format(escolhido))
#print('O(a) aluno(a) escolhido(a) foi: {}.'.format(random.choice(listaaluno)))
