#variaveis
vetor = []
soma = 0
for n in range(0, 20):
    valor = int(input("Informe um valor: "))
    vetor.append(valor)
    soma = soma + valor
print("Soma total é {0}.".format(soma)) 
