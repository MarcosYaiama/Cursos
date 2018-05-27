#include <stdio.h>
#include <math.h>

int parimpar(int numero){
  int resto = numero % 2;
  if(resto == 0) return 1;
  return 0;
}

int potencia(int a, int b){
	return pow(a,b);
}

int soma(int numeros[10]){
	int i;
	int soma = 0;
	for(i = 0;i < 10; i++){
		soma += numeros[i];
	}
	return soma;
}
int main(){
	int array[10];
	int c;
	for(c = 0;c < 10;c++){
		array[c] = c;
	}
	printf("%d ",soma(array));
}




