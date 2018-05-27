#include <stdio.h>
#include <string.h>

int main(){
	printf("***************************\n\n");
	printf("Bem vindo ao Jogo da Forca!\n\n");
	printf("***************************\n\n");
	char palavrasecreta[20];

	sprintf(palavrasecreta, "MELANCIA");
	
	printf(" _______\n");        
	printf(" |/      |\n");      
	printf(" |      (_)\n");  
	printf(" |      \\|/\n");  
	printf(" |       |\n");    
	printf(" |      / \\ \n");   
	printf(" |   	\n");           
	printf("_|___\n\n\n\n");

	printf("A palavra possui %d letras! Voce sabe qual eh a palavra?\n\n", strlen(palavrasecreta));
	
	char palavrasAcertadas[20];
	int acertou = 0;
	int enforcou = 0;
	int i;
	printf("O tamanho da variavel palavrasAcertadas eh %d\n",strlen(palavrasAcertadas));
	for(i = 0; i < strlen(palavrasecreta); i++){
		printf("_ ");
	}

	printf("\n\n");
	do{
		//comecar o jogo!!

		printf("\n\nQual o seu chute?");
		char chute;
		chute = getchar();
		
		for(i = 0; i < strlen(palavrasecreta); i++){
			if(chute == palavrasecreta[i]){
				printf("A posicao %d tem essa letra \n", i);
				palavrasAcertadas[i] = palavrasecreta[i];
			}
		}
		for(i = 0; i < strlen(palavrasecreta); i++){
			if(palavrasecreta[i] == palavrasAcertadas[i]){
				printf("%c ",palavrasAcertadas[i]);
			}else{
				printf("_ ");
			}
		}

		printf("\n\n");
		printf("O tamanho da variavel palavrasAcertadas eh %d",strlen(palavrasAcertadas));
		printf("\n\n");
		if(strlen(palavrasAcertadas) > strlen(palavrasecreta)){
			break;
		}

	}while(!acertou && !enforcou);
	printf("Fim de JOGO!");

}

/*
  _______        
 |/      |      
 |      (_)  
 |      \|/  
 |       |     
 |      / \   
 |              
_|___



    _______________         
   /               \       
  /                 \      
//                   \/\  
\|   XXXX     XXXX   | /   
 |   XXXX     XXXX   |/     
 |   XXX       XXX   |      
 |                   |      
 \__      XXX      __/     
   |\     XXX     /|       
   | |           | |        
   | I I I I I I I |        
   |  I I I I I I  |        
   \_             _/       
     \_         _/         
       \_______/






       ___________      
      '._==_==_=_.'     
      .-\:      /-.    
     | (|:.     |) |    
      '-|:.     |-'     
        \::.    /      
         '::. .'        
           ) (          
         _.' '._        
        '-------'
*/
