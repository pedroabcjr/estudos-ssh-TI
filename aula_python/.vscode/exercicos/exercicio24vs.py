#variaveis
contador_total = 0
contador_1 = 0
contador_2 = 0
contador_3 = 0
contador_4 = 0
#entrada
identificador = int(input("Informe a identificação do equipamento: "))
while identificador != 0:
    print ("1 - Necessidade de esfera.")
    print ("2 - Necessidade de limpeza.")
    print ("3 - Necessidade de troca de cabo ou conector.")
    print ("4 - Quebrado ou inutilizado.")
    defeito = int(input("Informe o defeito: "))
    if defeito == 1:
        contador_1 = contador_1 + 1
    elif defeito == 2:
        contador_2 = contador_2 + 1
    elif defeito == 3:
        contador_3 = contador_3 + 1    
    elif defeito == 4:
        contador_4 = contador_4 + 1
    contador_total = contador_total + 1
    identificador = int(input("Informe a identificação do equipamento: "))

#variaveis
p1 = contador_1 / contador_total * 100.0
p2 = contador_2 / contador_total * 100.0
p3 = contador_3 / contador_total * 100.0
p4 = contador_4 / contador_total * 100.0

print("Defeito                                    Quantidade        Percentual")
print("Necessidade de esfera                          {0}             {1:.2f}%".format(contador_1, p1))
print("Necessidade de limpeza                         {0}             {1:.2f}%".format(contador_2, p2))
print("Necessidade de troca de cabo ou conector       {0}             {1:.2f}%".format(contador_3, p3))
print("Quebrado ou inutilizado                        {0}             {1:.2f}%".format(contador_4, p4))















