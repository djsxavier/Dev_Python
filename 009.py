#Faça um algoritmo que leia quanto dinheiro uma pessoa tem na carteira (em R$) e mostre quantos dólares ela pode comprar. 
#Considere US$1,00 = R$3,45.

carteira = float(input("Quanto dinheiro você tem na carteira? R$ "))
taxa = 3.45
dolar = carteira / taxa
print("Com R$ {:.2f}, você pode comprar US$ {:.2f}.".format(carteira, dolar))
