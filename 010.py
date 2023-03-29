largura = float(input("Informe a largura: "))
altura = float(input("Informe a altura: "))
calculo = largura * altura
print ('Sua parede tem {} de largura e {} de altura e a sua área é de {} m²' .format (largura,altura,calculo))
tinta = calculo / 2
print ("Para pintar a parede, você precisa de {} litros de tinta" .format (tinta))