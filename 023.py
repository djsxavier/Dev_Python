#Numa promoção exclusiva para o Dia da Mulher, uma loja quer dar descontos para todos, mas especialmente para mulheres. 
#Faça um programa que leia nome, sexo e o valor das compras do cliente e calcule o preço com desconto. Sabendo que:
#- Homens ganham 5% de desconto
#- Mulheres ganham 13% de desconto
print('Digite o sexo sendo, M para masculino e F para Feminino')
nome = input('Digite o nome do cliente: ')
sexo = input('Digite o sexo do cliente: ')
compras = float(input('Valor total de compras do cliente: '))
if sexo == 'Masculino' or sexo == 'masculino':
    #r2 = s+(s*12.5/100)
    desc1 = compras + (compras*5/100)
    print('O valor com desconto será de R$ {}'.format(desc1))
elif sexo == 'Feminino' or sexo == 'feminino':
    desc2 = compras + (compras*13/100)
    print('O valor com desconto será de R$ {}'.format(desc2))