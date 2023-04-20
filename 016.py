dias = int(input("Quantidade de cigarros por dia: "))
anos = float(input("Quantidade de anos fumando: "))
minutos = anos * 365 * dias * 10
redução = minutos / (24 * 60)
print("Redução do tempo de vida {:.2f} dias." .format(redução))