#Faça um programa que leia a largura e o comprimento de um terreno retangular, calculando e mostrando a sua área em m². O programa 
#também devemostrar a classificação desse terreno, de acordo com a lista abaixo:
#- Abaixo de 100m² = TERRENO POPULAR
#- Entre 100m² e 500m² = TERRENO MASTER
#- Acima de 500m² = TERRENO VIP
l = float(input('Digite a largura do terreno: '))
c = float(input('Digite o comprimento do terreno: '))
area = l*c
if area < 100:
    print('Terreno popular')
elif area >= 100 and area <= 500:
    print('Terreno master')
elif area > 500:
    print('Terreno vip!')