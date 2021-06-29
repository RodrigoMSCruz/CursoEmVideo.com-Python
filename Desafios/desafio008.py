# Converte uma medida em m dada pelo usuário em centímetors e milímetros e exibe na tela.

# km    hm   dam m dm cm  mm
# 0.001 0.01 0.1 1 10 100 1000

metro = float(input('Digite a medida em metros(m): '))
km = metro * 0.001 #Mesmo que dividir por 1000.
hm = metro * 0.01  #Mesmo que dividir por 100.
dam = metro * 0.1  #Mesmo que dividir por 10.
dm = metro * 10
cm = metro * 100
mm = metro * 1000

print('A conversão de {}m para a as demais medidas fica: '.format(metro))

print('A medida em quilômtros (km) é {}.'.format(km))
print('A medida em hectômetro (hm) é {}.'.format(hm))
print('A medida em decâmetro (dam) é {}.'.format(dam))
print('A medida em decímetros (dm) é {}.'.format(dm))
print('A medida em centímetros (cm) é {}.'.format(cm))
print('A medida em milímetros (mm) é {}.'.format(mm))
