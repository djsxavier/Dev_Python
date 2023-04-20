#Escreva um programa que leia o ano de nascimento de um rapaz e mostre a sua situação em relação ao alistamento militar.
#- Se estiver antes dos 18 anos, mostre em quantos anos faltam para o alistamento.
#- Se já tiver depois dos 18 anos, mostre quantos anos já se passaram do alistamento.
ano = int(input('Ano de nascimento do rapaz: '))
calc = 2023-ano
if calc > 18:
    calc2 = calc-18
    print('Você precisa alistar, já se passaram {} anos'.format(calc2))
calc3 = 18-calc
print('Faltam {} para você se alistar'.format(calc3))