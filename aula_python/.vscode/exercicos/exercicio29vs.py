#variaveis
vetor = []
maiores_50 = False

#entrada /processamento
for n in range(0, 10):
    num = int(input("Informe {0}/10 número: ".format(n + 1)))
    vetor.append(num)
for n in vetor:
    if n > 50:
        print ("O número {0} está na posição {1} do vetor".format(n, vetor.index(n)))
        maiores_50 = True
    if maiores_50 == False:
        print ("Não existem valores maiore que 50.")



