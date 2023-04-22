#Refaça o algoritmo 25, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#- EQUILÁTERO: todos os lados iguais
#- ISÓSCELES: dois lados iguais
#- ESCALENO: todos os lados diferentes

a = int(input('Digite um valor de uma reta: '))
b = int(input('Digite outro valor de uma reta: '))
c = int(input('Digite mais um outro valor de uma reta: '))
if a < b + c and b < a + c and c < a + b:
    print('É possível criar um triângulo com estas retas')
else:
    print('Não será possível criar um triângulo com estas retas')
if a == b == c:
        print("O triângulo formado é EQUILÁTERO.")
elif a == b or a == c or b == c:
        print("O triângulo formado é ISÓSCELES.")
else:
        print("O triângulo formado é ESCALENO.")