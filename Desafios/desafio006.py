# Exibe o o dobro, o triplo e a raiz quadrada de um número que o usuário dá entrada.
n = int(input('Digite um número: '))
x2 = n * 2
x3 = n * 3
rq = n ** (1/2) #Raiz quadrada do número n. n elevado a 1/2.
#rq = pow(n,(1/2)) #Raiz quadrada também, usanod a função pow(). Exponenciação.
print('O número é: {} e seu dobro é {}, seu triplo é {} e sua raiz quadrada é {:.2f}'.format(n, x2, x3, rq))
