#entrada
numero = int(input("Informe um número de 1 a 10: "))
#processamento
while numero < 1 or numero >10:
    numero = int(input("Informe um número de 1 a 10: "))
print("Tabuada do nº {0}:".format(numero))
for n in range(1,11):
    print("{0} * {1} = {2}".format(numero, n, (numero * n)))
    