#include <stdio.h>
#include <stdlib.h>
#include <time.h>


void main(){
	printf("\n\n");
	printf("          P  /_\\  P                              \n");
	printf("         /_\\_|_|_/_\\                             \n");
	printf("     n_n | ||. .|| | n_n         Bem vindo ao    \n");
	printf("     |_|_|nnnn nnnn|_|_|     Jogo de Adivinhacao!\n");
	printf("    |" "  |  |_|  |"  " |                        \n");
	printf("    |_____| ' _ ' |_____|                        \n");
	printf("          \\__|_|__/                              \n");
	printf("\n\n");
	
	srand(time(0));
	int numerosecreto = rand() % 100;

	int chute;
	
	double pontos = 1000;
	int tentativa = 1;
	int acertou;

	int nivel;
	printf("Qual o nivel de dificuldade?\n");
	printf("(1) Facil (2) Medio (3) Dificil\n\n");
	printf("Escolha: ");
	scanf("%d", &nivel);
		
	int numerotentativas;
	switch(nivel) {
		case 1:
			numerotentativas = 20;
			break;
		case 2:
			numerotentativas = 15;
			break;
		default:
			numerotentativas = 6;
			break;
	}
	int i;
	for(i = 1; i <= numerotentativas; i++){
		printf("Tentativa %d de %d\n",i, numerotentativas);
		printf("Pontos = %.2f\n", pontos);
		
		printf("Qual o seu chute?? ");
		scanf("%d", &chute);
		
		double pontosPerdidos = abs(chute - numerosecreto)/2.0;
		printf("Pontos perdidos = %.2f\n",pontosPerdidos);


		if(chute < 0){
			printf("Você não pode chutar um numero abaixo de 0, tente outro numero!\n");
			i--;
			continue;
		}
		
		printf("O seu chute %d \n", chute);

		acertou = numerosecreto == chute;
		int menor = numerosecreto > chute;

		if(acertou){
			break;
		}

		else if(menor){													
			printf("Seu chute foi menor do que o número secreto, tente outra vez\n");
		}

		else{													
			printf("Seu chute foi maior do que o número secreto, tente outra vez\n");
		}
		
		pontos -= pontosPerdidos;
		
	}
	printf("FIM DE JOGO!\n");
	
	printf("\n");
	if(acertou) {
	    printf("             OOOOOOOOOOO               \n");
	    printf("         OOOOOOOOOOOOOOOOOOO           \n");
	    printf("      OOOOOO  OOOOOOOOO  OOOOOO        \n");
	    printf("    OOOOOO      OOOOO      OOOOOO      \n");
	    printf("  OOOOOOOO  #   OOOOO  #   OOOOOOOO    \n");
	    printf(" OOOOOOOOOO    OOOOOOO    OOOOOOOOOO   \n");
	    printf("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO  \n");
	    printf("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO  \n");
	    printf("OOOO  OOOOOOOOOOOOOOOOOOOOOOOOO  OOOO  \n");
	    printf(" OOOO  OOOOOOOOOOOOOOOOOOOOOOO  OOOO   \n");
	    printf("  OOOO   OOOOOOOOOOOOOOOOOOOO  OOOO    \n");
	    printf("    OOOOO   OOOOOOOOOOOOOOO   OOOO     \n");
	    printf("      OOOOOO   OOOOOOOOO   OOOOOO      \n");
	    printf("         OOOOOO         OOOOOO         \n");
	    printf("             OOOOOOOOOOOO              \n");
	    printf("\nParabens! Voce acertou!\n");
	    printf("Voce fez %.2f pontos. Ate a proxima!\n\n", pontos);
	} else {
	    printf("       \\|/ ____ \\|/    \n");   
	    printf("        @~/ ,. \\~@      \n");   
	    printf("       /_( \\__/ )_\\    \n");   
	    printf("          \\__U_/        \n");
	    printf("\nVoce perdeu! Tente novamente!\n\n");
	}
}