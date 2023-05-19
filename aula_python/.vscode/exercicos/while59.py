'''
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim

condicao = True

while condicao:
    nome = input('Qual o seu nome: ')
    print(f'Seu nome é {nome}')

    if nome == 'sair':
        break
print('Acabou')'''


#Repetições
#while (enquanto)
#Executa uma ação enquanto uma condição for verdadeira
#Loop infinito -> Quando um código não tem fim

'''continue  = pular o valor e break = para o loop

contador = 0

while contador <= 100:
    contador += 1

    if contador == 7:
        print("não irei mostrar o número 6.")
        continue

    if contador >= 10 and contador <= 30:
        print("Não irei mostrar", contador)
        continue

    if contador % 2 == 0:
       print(f"O número {contador} é par.")
    else:
        print(f"O número {contador} é ímpar.")

    if  contador == 8:
       break

    print(contador)
          
print('Acabou')

# Operadores de atribuição
# = += -= *= /= //= **= %=

contador = 10
###
contador /= 5
print(contador)

tabuada = int(input("Informa um número: "))
contador = 0

while contador <= 9:
    contador += 1
    conta = contador * tabuada
    print(f"{contador} * {tabuada} = {conta}")'''

#Repetições

##Executa uma ação enquanto uma condição for verdadeira
#Loop infinito -> Quando um código não tem fim

'''qtd_linhas = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas:
        print(f'{linha=} {coluna=}')
        coluna += 1
    linha += 1

print('Acabou')

qtd_linhas = 10
qtd_colunas = 10

linha = 1
while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas:
        print(f"{linha=}  {coluna=}")
        coluna += 1
    linha += 1
print("Acabou")
#        0123456789101112
nome  = "Pedro Junior"
tam_nome = len(nome)
print(nome)
print(tam_nome)
print(nome [6])

#EXERCÍCIO

nome = 'Pedro Junior'
indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1
novo_nome+='*'
print(novo_nome)'''





