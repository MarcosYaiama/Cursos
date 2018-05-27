#include <stdio.h>
#include <string.h>

char palavrasecreta[20];


void abertura(){
	printf("***************************\n\n");
	printf("Bem vindo ao Jogo da Forca!\n\n");
	printf("***************************\n\n");
}

void chuta(char chutes[26],int *tentativas){
	char chute;
	printf("Qual letra? ");
	scanf(" %c", &chute);

	chutes[(*tentativas)] = chute;
	(*tentativas)++;
}

void escolhePalavra(){
	sprintf(palavrasecreta, "MELANCIA");
}

int main(){
	int acertou = 0;

	int enforcou = 0;

	int tentativas = 0;
	char chutes[26];

	escolhePalavra();
	printf("%d %d\n", &chutes, chutes);
	printf("%d %d %d \n", &chutes[0],&chutes[1],&chutes[2] );

	abertura();
	
	do{
		//Imprime a palavra secreta
		int i;
		for(i = 0; i < strlen(palavrasecreta); i++){
			int j;
			int achou = 0;
			//Verifica o chute
			for(j = 0; j < tentativas; j++){
				if(chutes[j] == palavrasecreta[i]){
					achou = 1;
					break;
				}
			}

			if(achou){
				printf("%c ", palavrasecreta[i]);
			}else{
				printf("_ ");
			}
			
		}
		printf("\n");

		chuta(chutes, &tentativas);

	}while(!acertou && !enforcou);
}