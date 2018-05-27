#include <stdio.h>
#include <string.h>
#define TAMANHO_MAX 20 // Tamanho maximo dos arrays

// assinatura de funcao auxiliar
int tamLetrasCertas(char* palavrasAcertadas, int tamPalavraSecreta); 

// funcao auxiliar para calcular mais facilmente o numero de letras ja acertadas pelo usuario.
int tamArrayLetrasCertas(char* palavrasAcertadas, int tamPalavraSecreta) {
    int tam = 0;
    for(int i = 0; i < tamPalavraSecreta; i++) {
        if(palavrasAcertadas[i] != '0')
            tam++;
    }
    return tam;
}


int main(){
    printf("***************************\n\n");
    printf("Bem vindo ao Jogo da Forca!\n\n");
    printf("***************************\n\n");

    // array que guardara palavra a descobrir
    char palavrasecreta[TAMANHO_MAX];  

    // popula o array com a palavra a ser descoberta 
    sprintf(palavrasecreta, "MELANCIA"); 

    // desenha o boneco na forca :)
    printf(" _______\n");        
    printf(" |/      |\n");      
    printf(" |      (_)\n");  
    printf(" |      \\|/\n");  
    printf(" |       |\n");    
    printf(" |      / \\ \n");   
    printf(" |       \n");           
    printf("_|___\n\n\n\n");

    // como o strlen eh bastante usado, p/ haver só 1 chamada de funcao    
    int tamPalavraSecreta = strlen(palavrasecreta);

    printf("A palavra possui %d letras! Voce sabe qual eh a palavra?\n\n", tamPalavraSecreta);

    // guarda c/ letra digitada por quem esta tentando advinhar a palavra
    char palavrasAcertadas[TAMANHO_MAX]; 
    int acertou = 0;
    int enforcou = 0;
    int i;

    for(i = 0; i < tamPalavraSecreta; i++){
        printf("_ ");
    }
    // populando array dos chutes do usuario
    for(i = 0; i < TAMANHO_MAX; i++) { 
        palavrasAcertadas[i] = '0';
    }

    printf("\n\n");
    char chute = '0';

    // variavel auxiliar, para as iteracoes intermediarias
    int tamLetrasCertas = 0; 

    //comecar o jogo!!
    // se nao acertou e se ainda nao foi enforcado
    while(!acertou && enforcou < tamPalavraSecreta) { 
        printf("\nQual o seu chute?\n");

        acertou = 0;
        chute = getchar();

        printf("Chute = %c\n\n",chute);

        // verifica se o chute corresponde a ao menos uma letra da palavra secreta
        for(i = 0; i < tamPalavraSecreta; i++){
        // só recebe a letra quando o chute é verdadeiro.
            if(chute == palavrasecreta[i]){ 
                // i+1 = melhora indice da letra escrita na tela
                printf("A posicao %d tem essa letra\n", i+1); 
                palavrasAcertadas[i] = palavrasecreta[i];
                acertou = 1;
            } 
        }
        // se nao acertou o chute, maior chance de ser enforcado
        if(!acertou) { 
            enforcou++;
        }

        for(i = 0; i < tamPalavraSecreta; i++){
            if(palavrasecreta[i] == palavrasAcertadas[i]){
                printf("%c ",palavrasAcertadas[i]);
            }else{
                printf("_ ");
            }
        }

        tamLetrasCertas = tamArrayLetrasCertas(palavrasAcertadas, tamPalavraSecreta);

        printf("\n");
        printf("\nO tamanho da variavel palavrasAcertadas eh %d", tamLetrasCertas);
        printf("\nChances para nao ser enforcado: %d",(tamPalavraSecreta-enforcou));
        printf("\n\n======================================\n");

      // igual se 'palavras acertadas é igual a palavra secreta'  
      if(tamLetrasCertas >= tamPalavraSecreta){ 
            acertou = 1;
        } else {
            // limpa varivel que pode ter sido mudada antes e continuar o loop
            acertou = 0; 
        }
    }
    printf("\n\nFim de JOGO!\n");
    if(enforcou >= tamPalavraSecreta) {
        printf("Nao deu! Voce foi enforcado e perdeu!");
    } else if(acertou) {
        printf("Parabens! Voce venceu o jogo!");
    }
}

