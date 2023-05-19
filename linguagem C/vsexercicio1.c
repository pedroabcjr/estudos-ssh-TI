#include <stdio.h> 
#include <string.h>

int main(){
    char login[100], senha[100];

	printf("informe o login: ");
	gets(login);
	printf("informe a senha: ");
	gets(senha);

    while(!strcmp(login, senha)){
    	printf("nome de usuario deve ser diferente da senha.\n");
    	printf("informe o login: ");
    	gets(login);
    	printf("informe a senha: ");
    	gets(senha);
	}

}
