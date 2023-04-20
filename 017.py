velocidade = int(input('Qual a sua velocidade? '))
if velocidade > 80:
    print('Você foi multado')
    multa = (velocidade-80)*5
    print('Você vai pagar R$ {:.2f} de multa'.format(multa)) 
print('Você não foi multado!')