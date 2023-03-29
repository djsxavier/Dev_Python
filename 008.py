distancia = float (input('Digite uma distância em metros: '))
km = distancia / 1000
hm = distancia  /100
dm = distancia * 10
cm = distancia * 100
dam = distancia / 10
mm = distancia * 1000
print ('{} KM, {} HM, {} DM, {} CM, {} DAM, {} MM' .format(km,hm,dm,cm,dam,mm))
