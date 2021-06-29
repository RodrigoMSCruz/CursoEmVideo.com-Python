# Calcula a hipotenusa com os valores dos catetos inseridos pelo usuário.

from math import pow, sqrt
#from math import hypot
catetooposto = float(input('Digite o valor do cateto oposto: '))
catetoadjacente = float(input('Digite o valor do cateto adjacente: '))

hipotenusa = sqrt(pow(catetooposto,2) + pow(catetoadjacente,2))
#hipotenusa = ((catetooposto **2) + (catetoadjacente ** 2)) ** 1/2
#hipotenusa = hypot(catetooposto,catetoadjacente)

print('O valor da hipotenusa é: {}'.format(hipotenusa))

