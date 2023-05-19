#variaveis
vetor = []
codigo = int(input("Informe o código: "))
if codigo != 0:
    for n in range(0, 5):
        valor = float(input("digite um valor: "))
        vetor.append(valor)
    if codigo == 1:
        vetor.reverse()
        for n in vetor:
            print(n) 
    if codigo == 2:
        for n in vetor:
            print(n)



