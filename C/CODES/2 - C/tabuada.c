#include <stdio.h>

void main(){
	float x;
	int opc;

	while(1){
		int i;
		while(1){	
			printf("Vamos calcular a tabuada?");
			printf("(0) NAO  (1)SIM\n");
			scanf("%d", &opc);
			if(opc != 1 && opc != 0){
				printf("Nao torne as coisas dificeis, digite uma OPCAO VALIDA!\n");
				continue;
			}
			else if(opc != 1){
				printf("Que pena :( fica pra proxima entao!\n");
				break;
			}
			printf("Otimo, vamos usar o numero que voce digitar e calcular sua tabuada de 0 ate 10!\n");
			printf("Qual numero deseja que a variavel x absorva para iniciarmos nossa tabuada?\n");
			scanf("%f", &x);

			printf("Muito bem! O numero escolhido foi %.2f\n", x);
			printf("*****TABUADA DO %.2f*********\n");
			for(i = 0; i < 11; i++){
			printf("%.2f x  %d = %.2f\n", x, i , x * i);
			}
			break;
		}
		if(opc != 1){
			break;
		}
		printf("Deseja fazer a tabuada de outro numero?\n");
		printf("Digite 1 para fazer outra tabuada ou aperte qualquer NUMERO para finalizar o programa\n");
		scanf("%d", &opc);
		if(opc != 1){
			printf("Foi um prazer calcular com voce, ate a proxima!\n");
			break;
		}
	}

}