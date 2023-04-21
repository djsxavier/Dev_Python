#Escreva um algoritmo que leia dois números inteiros e compare-os, mostrando na tela uma das mensagens abaixo: 
#- O primeiro valor é o maior
#- O segundo valor é o maior
#- Não existe valor maior, os dois são iguais

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
if num1 > num2:
    print('O primeiro número é maior')
elif num2 > num1:
    print('O segundo número é o maior')
elif num1 == num2:
    print('Não existe número maior, os dois são iguais')