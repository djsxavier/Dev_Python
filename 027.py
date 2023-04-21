#Crie um programa que leia duas notas de um aluno e calcule a sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#- Média até 4.9: REPROVADO
#- Média entre 5.0 e 6.9: RECUPERAÇÃO
#- Média 7.0 ou superior: APROVADO

n1 = int(input('Digite a primeira nota: '))
n2 = int(input('Digite a segunda nota: '))
media = (n1+n2)/2
if media < 5:
    print('Reprovado!')
elif media > 5 and media < 7:
    print('Recuperação!')
elif media >= 7:
    print('Aprovado!')