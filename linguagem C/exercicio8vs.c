#include <stdio.h>

int main(){
    //Variáveis
    int vetor[10];
    char tem_maior_50;

//Entradas
    for(int i = 0; i < 10; i++){
    printf("informe um valor para o vetor %d/10 ", (i + 1));
    scanf("%d", &vetor[i]);

    }
    for (int i = 0; i < 10; i++){
        if(vetor[i] > 50){
            printf("O numero %d está na posição %d\n", vetor[i], i);
            tem_maior_50 = 1;
        }
    }  
    if(tem_maior_50 < 1){
        printf("Não há valor maior que 50.");
    }
}
