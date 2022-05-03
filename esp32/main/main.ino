#include "HX711.h"  

/*
 * DOUT  - 35
 * P_SCK - 34
 */
HX711 scale;

void setup() {
  // put your setup code here, to run once:

  Serial.begin(9600);
  scale.begin(35, 34);
  
  Serial.println("Mantenha a balança vazia");
  Serial.println("Tarando...");
  delay(3000);
  Serial.print("Peso da prateleira: ");
  Serial.println(scale.read_average(20));
  scale.tare();

}

void loop() {
  // put your main code here, to run repeatedly:

  Serial.println(scale.read_average(20));
  delay(500);
}
