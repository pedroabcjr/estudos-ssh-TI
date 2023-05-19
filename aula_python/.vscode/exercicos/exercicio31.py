 
#aula sobre if elif e else
#variavel
login = 'não'
#entrada
acesso = input("Você deseja acessar o sistema '(sim/não)': ")
#processento
if acesso == "sim":
    print ("Você esta logado.")
elif acesso == login:
    print("Acesso deslogado.")
elif acesso != login:
    acesso = input("Você deseja acessar o sistema '(sim/não)': ")
    if acesso == "sim":
        print ("Você esta logado.")
    elif acesso == login:
        print("Acesso deslogado.")
elif acesso == login:
    print("Acesso deslogado.")





    

    


           