#velocidade, a multa e a diferença de velocidade
v = int(input('Digite sua velocidade: '))
if v > 80:
    print('Você foi multado!')
    d = v - 80
    multa = d*5
    print('Você passou {} km acima da velocidade.\n Sua multa é no valor de R$ {}'.format(d,multa))
else:
    print('Parabéns, sua velocidade está ótima!')