#include <stdio.h>
#include <stdlib.h>

void main(){
	while(1){
		printf("Que tipo de operacao deseja realizar?\n");
		printf("(1)SOMA  (2)SUBTRACAO   (3)DIVISAO    (4) MULTIPLICACAO\n");
		int op;
		scanf("%d", &op);
		printf("Voce escolheu a operacao: %d\n", op);

		float n1;
		float n2;
		int nova;
		
		while(op <= 0 || op > 4){
			printf("Opcao invalida, escolha uma operacao:\n");
			printf("(1)SOMA  (2)SUBTRACAO   (3)DIVISAO    (4) MULTIPLICACAO\n");
			scanf("%d", &op);
			if(op > 0 && op < 5){
				break;
			}
		}
		
			if(op == 1){
				printf("Voce escolheu soma, quais numeros vamos calcular? \n\n");
			}
			else if(op == 2){
				printf("Voce escolheu subtracao, quais numeros vamos calcular? \n\n");
			}
			else if(op == 3){
				printf("Voce escolheu divisao, quais numeros vamos calcular? \n\n");
			}
			else if(op == 4){
				printf("Voce escolheu multiplicacao, quais numeros vamos calcular? \n\n");
			}
		
		
		printf("Escolha dois numeros para o calculo, digite o primeiro numero: \n");
		scanf("%f", &n1);
		printf("Digite outro numero fazer a operacao com %.2f, insira o segundo numero: \n",op ,n1);
		scanf("%f", &n2);

		float resp;
		while(op > 0 && op < 5){

			if(op == 1){
				resp = n1 + n2;
				printf("A adicao resultou em: %.2f + %.2f = %.2f\n",n1 , n2, resp);
			}
			if(op == 2){
				resp = n1 - n2;
				printf("A subtracao resultou em: %.2f - %.2f = %.2f\n",n1 , n2, resp);
			}
			if(op == 3){
				resp = n1 / n2;
				printf("A divisao resultou em: %.2f / %.2f = %.2f\n",n1 , n2, resp);
			}
			if(op == 4){
				resp = n1 * n2;
				printf("A multiplicacao resultou em: %.2f x %.2f = %.2f\n",n1 , n2, resp);
			}
			break;
		}
		
		printf("Deseja realizar outra operacao? \n");
		printf("(0)NAO     (1)SIM \n");
		scanf("%d", &nova);
		if(nova == 0){
			printf("Obrigado por calcular!");
			break;
		}
	}
}