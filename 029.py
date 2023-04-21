#Desenvolva um programa que leia o nome de um funcionário, seu salário, quantos anos ele trabalha na empresa e mostre seu novo salário, 
#reajustado de acordo com a tabela a seguir:
#- Até 3 anos de empresa: aumento de 3%
#- entre 3 e 10 anos: aumento de 12.5%
#- 10 anos ou mais: aumento de 20%

n = input('Qual o nome do funcionário? ')
s = float(input('Qual o salário do funcionário? '))
a = int(input('Quantos anos o funcionário trabalha na empresa? '))
if a < 3:
    r1 = s+(s*3/100)
    print('Você teve um aumento de R$ {}'.format(r1))
elif a >= 3 and a < 10:
    r2 = s+(s*12.5/100)
    print('Você teve um aumento de R$ {}'.format(r2))
elif a >=10:
    r3 = s+(s*20/100)
    print('Você teve um aumento de R$ {}'.format(r3))