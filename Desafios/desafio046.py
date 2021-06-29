# Faz uma contagem regressiva de 10 segundos para o disparo de fogos de artífico.

from time import sleep

for i in range(10, -1, -1): # Lembrando que no "FOR", os parãmetros são, começo, fim e passo, sendo que o FOR para um passo antes do fim.
    print(i)
    sleep(1)
print('FOGO!')