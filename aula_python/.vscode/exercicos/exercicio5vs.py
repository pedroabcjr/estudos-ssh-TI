#entradas
valor_hora_trabalhada = float(input("Informe o valor da hora trabalhada: "))
horas_trabalhadas = int(input("informe a quantidade de horas trabalhadas: "))
#processamento 
calcula_hora = (valor_hora_trabalhada * horas_trabalhadas)
#saida
print("O salário a perceber é de {0:.2f}".format (calcula_hora))
