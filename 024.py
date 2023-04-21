#Faça um algoritmo que pergunte a distância que um passageiro deseja percorrer em Km. Calcule o preço da passagem, cobrando R$0.50 
#por Km para viagens até 200Km e R$0.45 para viagens mais longas.

distancia = float(input('Qual a distância que você deseja percorrer em KM? '))
if distancia <= 200:
    v1 = distancia *  0.50
    print('O valor da viagem é de R$ {}'.format(v1))
elif distancia > 200:
    v2 = distancia * 0.45
    print('O valor da viagem é de R$ {}'.format(v2))