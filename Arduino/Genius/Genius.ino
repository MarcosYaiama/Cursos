//Leds
#define N_LED 4
#define LED1 2
#define LED2 3
#define LED3 4
#define LED4 5
int leds[] = {LED1, LED2, LED3, LED4};

//Botoes
#define N_BTN 4
#define BTN1 6
#define BTN2 7
#define BTN3 8
#define BTN4 9
int btns[] = {BTN1, BTN2, BTN3, BTN4};
int estadoBTN[] = {0,0,0,0};
String btn_nomes[] = {"BTN1", "BTN2", "BTN3","BTN4"};

void setup(){

  Serial.begin(9600);
  definePortas(leds, btns);

for(int i = 0; i < 4; i++){
  Serial.println(leds[i]);
}
}

void loop(){
  alteraEstadoBTN();
}
