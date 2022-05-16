#include "HX711.h"  

/*
 * DOUT  - 35
 * P_SCK - 34
 */
HX711 scale;


// 2. Adjustment settings
const long LOADCELL_OFFSET = 50682624;
const long LOADCELL_DIVIDER = 5895655;

void setup() {
  // put your setup code here, to run once:

  Serial.begin(9600);
  scale.begin(35, 34);
  scale.set_scale(LOADCELL_DIVIDER);
  scale.set_offset(LOADCELL_OFFSET);
  
  Serial.println("Mantenha a balança vazia");
  Serial.println("Tarando...");
  delay(3000);
  scale.tare();

}

void loop() {
  // put your main code here, to run repeatedly:

  Serial.println(scale.get_units(10), 2);
  delay(500);
}
