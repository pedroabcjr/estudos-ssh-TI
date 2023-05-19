# Operador Logico "and"
'''entrada = input("[E]ntrar [S]air: ")
senha_de_entrada = input ("digite sua senha: ")
senha_permitida = "123456"

if entrada == "E" or entrada == "e" and senha_de_entrada == senha_permitida:
    print ('Entrar') 
else:
    print ("Sair")'''

#Operador Lógico "or"

'''entrada = input("[E]ntrar [S]air: ")
senha_de_entrada = input ("digite sua senha: ")
senha_permitida = "123456"

if (entrada == "E" or entrada == "e") and senha_de_entrada == senha_permitida:
    print ('Entrar') 
else:
    print ("Sair")'''

# Operador Lógico "not"

'''senha = 123456

codigo = input("digite sua senha: ")

if senha == codigo:
    print ("Logado")
if not codigo:
    print ("Você não digitou senha")'''

#Operadores Logicos "in" e "not in"
'''strings sãoiteraveis
 0  1  2  3  4  5 
 O  t  á  v  i  o 
-6 -5 -4 -3 -2 -1
nome = "Otávio"
print("tá" in nome)
print ("O" not in nome)


#Interpolação básic de strings

nome = "Pedro"
preco = 1000.95876732
variavel = "%s, o preço total foi R$%.2f" % (nome, preco)
print (variavel)
print("O hexadecimal do %d é %08X" %(1500, 1500))

# Formatação de Strings

variavel = "ABC"
print(f"{variavel}")
print(f"{variavel: >10}")
print(f"{variavel: <10}")
print(f"{variavel: ^10}")

#Fatiamento de Strings

 012345678
 Olá Mundo
-987654321
Obs: a função len retorna a qtd de caracteres da str

variavel = "Olá Mundo"
print(variavel[0:5] )
print(len(variavel[0:6:2])

nome = input("Informe seu nome: ")
idade = input("Informe sua idade: ")

if nome and idade:
    print(f"Seu nome é {nome}")
    print(f"Seu nome invertido é {nome[-1:-13:-1]}")
    if " " in nome:
        print("Nome contem espaços")
    else:
        print("Nome não contem espaços")    
    print(f"seu nome contem {len(nome)} letras")
    print(f'a primeira letra do seu nome {nome[0]}')
    print(f'A ultima letra do seu nome {nome[11]}')
else:
    print ("Você não digitou nada")'''
    
    #INTRODUÇÃO AO TRY / EXCEPT
'''try tentar executar o codigo
   except = ocorreu algum erro ao tentar executar

numero_str = input("O numero que digitar será dobrado: ")

try:
    numero_float = float(numero_str)
    print ("FLOAT", numero_float)
    print(f"O dobro do numero {numero_float} é {numero_float * 2}.")
except:
    print(" O valor informado não é aceitável.")

#   

# variaveis constantes

LIMITE_DE_VELOCIDADE = 60
LOCAL_RADAR = 100
PERIMETRO_RADAR = 1

# entradas

velociade_do_veiculo = input("Informe a velocidade do veículo: ")
local_veiculo = input("Informe qual KM está localizado o veículo: ")
velocidade_float = float(velociade_do_veiculo)
local_float = float(local_veiculo)

# processamento

if local_float >= 99 and local_float <= 101:
    if velocidade_float > LIMITE_DE_VELOCIDADE:
        print("Você ultrapassou o limite de velocidade e será multado")
    else:
        print("Dentro do limite de velocidade.")
else:
    print("Fora da área de monitoramento")'''

'''como verificar a id das variaveis... 

nome = "Pedro"
nome_2 = "Pedro JR"
print(id(nome))
print(id(nome_2))

#Flags Marcar um local - None (is Not, is)

condicao = True 
passou_no_if = None
if condicao:
    passou_no_if = True
    print("Faça algo")
else:
    print("Não faça algo")
    
print(passou_no_if, passou_no_if is  None)
print(passou_no_if, passou_no_if is not None)

#Variáveis
RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1
velocidade = 60
local_carro = 102
carro_multado = local_carro >= (LOCAL_1 -RADAR_RANGE) and \
      local_carro <= (LOCAL_1 + RADAR_RANGE) and \
        velocidade > RADAR_1
carro_nao_multado = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
      local_carro <= (LOCAL_1 + RADAR_RANGE) and \
        velocidade <= RADAR_1

#processamento
if carro_multado:
    print("Você passou acima da velocidade máxima")
elif carro_nao_multado:
    print("Dentro do limite de velocidade")
else:
    print("Fora de área do radar.")

#Flags Marcar um local - None = não valor (is Not, is)

condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print("Faça algo")
else:
    print("Não faça algo")
    
print(passou_no_if, passou_no_if is None)
print(passou_no_if, passou_no_if is not None)

#EXERCICIO 1 DA AULA 54

valor = input("Digite um número inteiro: ")

if valor.isdigit():
    valor_int = int(valor)
    par_impar = valor_int % 2 == 0
    par_impar_texto = "ìmpar"
    if par_impar:
        par_impar_texto = "par"
    
    print(f"Este número {valor_int} é {par_impar_texto}.")
    
else:
        print("Digite um número inteiro!")

try:
    valor_int = float(valor)
    par_impar = valor_int % 2 == 0
    par_impar_texto = "ìmpar"
    if par_impar:
        par_impar_texto = "par"
    
    print(f"Este número {valor_int} é {par_impar_texto}.")
    
except:
        print("Digite um número inteiro!")

#EXERCICIO 2 DA AULA 54

#entrada

'''

'''hora = float(input("Informe a hora: "))

if hora >= 0 and hora <= 24:
    if hora >= 0 and hora <= 11:
        print("Bom dia!")
    elif hora >= 12 and hora <= 17:
        print("Boa tarde!")
    elif hora >= 18 and hora <= 23:
        print("Boa noite!")
else:
    print(" digite uma hora válida!")

hora_1 = input("Informe a hora: ")

try:
    hora  = int(hora_1)

    if hora >= 0 and hora <= 11:
        print("Bom dia!")
    elif hora >= 12 and hora <= 17:
        print("Boa tarde!")
    elif hora >= 18 and hora <= 23:
        print("Boa noite!")
    else:
        print("Não conheço esta hora")

except:
    print("Digite uma hora válida!")

#EXERCICIO 3 DA AULA 54

nome = input("Informe seu nome:")
nome_1 = len(nome)

if nome_1 > 0 and nome_1 <= 4:
    print("seu nome é curto.")
elif nome_1 > 4 and nome_1 <= 6:
    print("seu nome é normal.")
elif nome_1 > 6:
    print("seu nome é grande.")
else:
    print("Digíte um nome!")'''

"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""
string = '1000'
# outra_variavel = f'{string[:3]}ABC{string[4:]}'
# print(string)
# print(outra_variavel)
print(string.zfill(10))
