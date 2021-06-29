# Calcula o IMC (Indíce de Massa Corporal) do usuário a partir das entradas
# do peso e da altura do mesmo.

peso = float(input('Digite o peso(kg) da pessoa: '))
altura = float(input('Digite a altura(m) da pessoa: '))
imc = peso / (altura ** 2) #  também pode ser usado pow(altura, 2) -> pow=potenciação -> Altura elevado a 2.
print('Seu IMC é gual a: {:.2f}.'.format(imc))

if imc < 18.5:
    print('Abaixo do peso.')
elif 18.5 <= imc < 25:
    print('Peso ideal.')
elif 25 <= imc < 30:
    print('Sobrepeso.')
elif 30 <= imc < 40:
    print('Obesidade.')
elif imc > 40:
    print('Obesidade mórbida.')
