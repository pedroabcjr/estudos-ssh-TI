#processamento/entrada
nome = input("Informe seu nome ")
senha = input("Informe sua senha ")
while senha == nome:
    print ("senha não pode ser igual ao nome.")
    nome = input("Informe seu nome ")
    senha = input("Informe sua senha ")
else:
    print ("confirmado login.")