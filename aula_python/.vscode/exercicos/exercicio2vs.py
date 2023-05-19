#entradas
quantidade_minima = int(input("Informe a quantidade mínima"))
quantidade_maxima = int(input("Informe a quantidade máxima"))

#processamento
estoque = (quantidade_minima + quantidade_maxima) / 2

#saida
print ("A quantidade média do estoque é {0}." .format (estoque))
