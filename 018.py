#Faça um programa que leia o ano de nascimento de uma pessoa, calcule a idade dela e depois mostre se ela pode ou não votar.
nasc = int(input('Qual a seu ano de nascimento? '))
idade = 2023-nasc
if idade > 18:
    print('Você pode votar')
print('Você ainda não pode votar, porque você tem {} anos'.format(idade))