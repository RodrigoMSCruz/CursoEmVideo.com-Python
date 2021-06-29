# Programa que tenha uma função chamada voto() que recebe como parâmetro o ano de nascimento de uma
# pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

def voto(ano):
    from datetime import date

    idade = date.today().year - ano
    if idade < 16:
        return f'Com {idade} anos: VOTO NEGADO'
    elif 16 <= idade < 18:
        return f'Com {idade} anos: VOTO OPCIONAL'
    elif 18 <= idade <= 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'
    elif idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
#end-def


ano = int(input('Em que ano você nasceu? '))
print(f'{voto(ano)}')