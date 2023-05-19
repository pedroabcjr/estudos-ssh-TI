#variaveis
vetor = []
pares = []

#entrada

n = int(input("Informe um número: "))

#processamento
while n != 0:
    vetor.append(n)
    if n % 2 == 0:
        p = n
        pares.append(p)
    n = int(input("Informe um número: "))
for p in pares:
    print(p)


