#Faça um algoritmo que leia um determinado ano e mostre se ele é ou não BISSEXTO.
ano = int(input('Digite um ano: '))
if ano %4 ==0 and ano %100 != 0 or ano %400 ==0:
    print('O ano é bissexto')
print('O ano não é bissexto')

#||
#&&