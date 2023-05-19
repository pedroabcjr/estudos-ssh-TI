#entradas
idade = int(input("Informe sua idade: "))
#processamento
if idade > 4 and idade <= 7:
    print("Infantil A")
elif idade > 7 and idade <= 11:
    print("Infantil B")
elif idade > 11 and idade <= 13:
    print("Juvenil A")
elif idade > 13 and idade <= 17:
    print("Juvenil B")
elif idade > 17:
    print("Adulto")