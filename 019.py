#Crie um algoritmo que leia o nome e as duas notas de um aluno, calcule a sua média e mostre na tela. No final, 
#analise a média e mostre se o aluno teve ou não um bom aproveitamento (se ficou acima da média 7.0).
nome = input('Qual o seu nome? ')
nota1 = float(input('Qual a sua nota? '))
nota2 = float(input('Qual a sua segunda nota? '))
media = (nota1+nota2)/2
if media >= 7:
    print('Parabéns {}, você é um bom aluno'.format(nome))
print('Você precisa estudar mais!')