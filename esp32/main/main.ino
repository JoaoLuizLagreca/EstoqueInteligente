#include "HX711.h"

#define DT 33
#define SCK 32


HX711 scale;


// 2. Adjustment settings
const long LOADCELL_OFFSET = 50682624;
const long LOADCELL_DIVIDER = 5895655;


const float desvio=0.000015;
float peso_produto;
void setup() {
  // put your setup code here, to run once:

  Serial.begin(9600);
  scale.begin(DT, SCK);
  scale.set_scale(LOADCELL_DIVIDER);
  scale.set_offset(LOADCELL_OFFSET);

  Serial.println("Mantenha a balança vazia");
  Serial.println("Tarando...");
  delay(3000);
  scale.tare();

  Serial.println("Coloque 1 item na prateleira");
  while(scale.get_units(10)<desvio){
    delay(500);
  }
  Serial.println("Medindo produto...");
  delay(1000);
  peso_produto=scale.get_units(10);
  Serial.print("Peso do produto: "); Serial.println(peso_produto, 5);
}

void loop() {
  // put your main code here, to run repeatedly:

  float p = scale.get_units(10);

  Serial.print("Produtos na prateleira: "); Serial.println(floor(p/peso_produto));
  delay(200);
}
