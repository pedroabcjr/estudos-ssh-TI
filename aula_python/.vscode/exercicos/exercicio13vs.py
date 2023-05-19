#entradas
c = int(input("Informe o código: "))
n = int(input("Informe o número de horas trabalhadas: "))
#processamento
if n > 50:
    e = (n - 50)
    hora_extra = e * 20.00
    n = (n - e) * 10.00
else:
    e = 0
    hora_extra = e * 0
    n = n * 10.00

print("Salário a receber {0:.2f}.".format(n))
print("Valor a receber de hora extra {0:.2f}.".format(hora_extra))

salario_total = n + hora_extra
print("salario total é de {0:.2f}.".format(salario_total))



