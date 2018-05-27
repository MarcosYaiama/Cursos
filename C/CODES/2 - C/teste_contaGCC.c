#include <stdio.h>
#include <stdlib.h>

void main(){
	int x;
	int y;

	printf("Primeiro num\n");
	scanf("%d",&x);
	printf("Segundo num\n");
	scanf("%d",&y);

	int oper1 = x + y;
	int oper2 = x - y;
	int oper3 = x / y;
	printf("SOMA: %d, SUBTRACAO %d, DIVISAO %d",oper1, oper2, oper3);
}