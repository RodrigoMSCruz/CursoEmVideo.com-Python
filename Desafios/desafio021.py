#Toca um arquivo mp3.

import pygame, time

pygame.init()
pygame.mixer.music.load('desafio021.mp3')
pygame.mixer.music.play()
#pygame.event.wait()
time.sleep(300) #Faz o programa aguardar por 5 minutos(Tempo em segundos - 5 x 60 = 300)
# A implemnetação original não funcionou, apesar do código ao usado pelo Guanabara no curso de Python.
# O time.sleep foi acrescentado por mim e foi o jeito que encontrei para fazêlo tocar a música.
# 5 minutos foi o tempo estimado para mim que dá para tocar uma boa média de músicas.
# A música em questão é do encerramento de um anime que assistia na epoca em que fiz essse código.
