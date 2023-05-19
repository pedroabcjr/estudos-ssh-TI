#aula sobre o "and"
#variavel
senha = 1234
acessar_sistema = input("Acessar o sistema - sim ou não: ")
if acessar_sistema == "sim":
    senha_de_acesso = int(input("Digite senha:"))
    if senha_de_acesso == senha:
        print("Você esta logado")
    elif senha_de_acesso != senha:
        print("Senha incorreta")
else:
    print("Deslogado")
