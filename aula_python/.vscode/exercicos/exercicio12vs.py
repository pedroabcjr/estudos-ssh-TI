# variaveis
e = 0
m = 0
#entradas
peso = int(input("informe o peso pescado: "))
#processamento
if peso > 50:
    e = peso - 50
    m = e * 4   
else:
    e = 0
    m = 0

print("O peso total é de {0} kg.".format(peso))
print("O peso excedente é de {0} kg.".format(e))
print("O valor da multa é de {0}.".format(m))

