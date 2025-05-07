#include <stdio.h>
int main() {
int numero_secreto=55;
int palpite;
int tentativas=0;

printf("Bem vindo ao jogo :)\n");
printf("Tente adivinhar um numero entre 1 a 100\n");
while(1){
    printf("Qual o seu palpite?");
    scanf("%d", &palpite);
    tentativas++;
    if (palpite > numero_secreto){
        printf("Calma, Sherlok!Esta muito alto.\n");
    } else if (palpite<numero_secreto){
        printf("Esta muito baixo, suba mais um pouco!\n");
    } else{
        printf("Agora sim!Finalmente voce acertou, parabens!");
        printf("Voce acertou em %d tentativas.\n", tentativas);
        break;
    }
}
return 0;
}
