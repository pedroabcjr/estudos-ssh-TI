#aula de "or"
'''#considerando que a idade militar é de 18 a 50 aos, cria uma aplicação que verifique
se a pessoa encontra-se em idade militar'''
#variavel
idade = 18
#entrada
informe_sua_idade = int(input("Informe sua idade: "))
#processamento 
if informe_sua_idade < idade or informe_sua_idade > 50:
    print("Dispensado.")
else:
    print ("Idade militar.")
