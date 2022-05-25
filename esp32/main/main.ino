#include "HX711.h"
#include <WiFi.h>

#define DT 33
#define SCK 32

const char* ssid = "WiFi ESP32"
const char* wifi_password = "esp446923"

// 2. Adjustment settings
const long LOADCELL_OFFSET = 50682624;
const long LOADCELL_DIVIDER = 5895655;



TaskHandle_t Core0T;
TaskHandle_t Core1T;

HX711 scale;




const float desvio=0.000015;
float peso_produto;
void setup() {
  // put your setup code here, to run once:

  Serial.begin(9600);

  xTaskCreatePinnedToCore(NetworkHandle, "CPU 0", 1000, NULL, 1, &Core0T, 0);
  xTaskCreatePinnedToCore(SensorHandle, "CPU 1", 1000, NULL, 1, &Core1T, 1);
  
}

void NetworkHandle(void * pr){
  while (true){
    delay(1);
  }
}

void SensorHandle(void * pr){
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

  float p;
  while (true){
    p = scale.get_units(10);

    Serial.print("Produtos na prateleira: "); Serial.println(floor(p/peso_produto));
    delay(200);
  }
  
}

void loop() {
  delay(0);
}
