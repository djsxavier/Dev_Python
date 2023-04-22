#[DESAFIO] Crie um programa que leia o tamanho de três segmentos de reta. Analise seus comprimentos e diga se é possível 
#formar um triângulo com essas retas. Matematicamente, para três segmentos formarem um triângulo, o comprimento de cada lado deve 
#ser menor que a soma dos outros dois.

a = int(input('Digite um valor de uma reta: '))
b = int(input('Digite outro valor de uma reta: '))
c = int(input('Digite mais um outro valor de uma reta: '))
if a < b + c and b < a + c and c < a + b:
    print('É possível criar um triângulo com estas retas')
else:
    print('Não será possível criar um triângulo com estas retas')
