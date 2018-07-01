void definePortas(int* leds, int* btns){
  for(int i = 0; i < 4; i++){
int porta = leds[i];
    pinMode(porta, 1);
  }

  for(int i = 0; i < N_LED; i++){
int porta = btns[i];
    pinMode(porta, INPUT_PULLUP);
  }
}

void alteraEstadoBTN(){
  static unsigned long tempobtn = 0;
  for(short i = 0; i < N_LED; i++){
    if((millis() - tempobtn) > 100){
      if(digitalRead(btns[i]) != estadoBTN[i]){
        estadoBTN[i] = digitalRead(btns[i]);
        piscaLed(leds[i], 500);
        Serial.print(btn_nomes[i] + " ");
        Serial.println(estadoBTN[i]);
      }
      tempobtn = millis();
    }
  }
}

void piscaLed(short led, short tempo){
  digitalWrite(led, 1);
  delay(300);
  digitalWrite(led, 0);
}

void feedLed(){


}
