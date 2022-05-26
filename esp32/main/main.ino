#include "HX711.h"
#include <WiFi.h>

#define DT 33
#define SCK 32

const char* ssid = "WiFi ESP32";
const char* wifi_password = "esp446923"; // Método prototipal, em um modelo de lançamento, o produto deveria apresentar uma interface de configuração para conectar à uma rede

// 2. Adjustment settings
const long LOADCELL_OFFSET = 50682624;
const long LOADCELL_DIVIDER = 5895655;



TaskHandle_t Core0T;
TaskHandle_t Core1T;

HX711 scale;
float peso;


const float desvio=0.000015;
void setup() {
  // put your setup code here, to run once:

  Serial.begin(9600);

  xTaskCreatePinnedToCore(NetworkHandle, "CPU 0", 5200, NULL, 1, &Core0T, 0);
  xTaskCreatePinnedToCore(SensorHandle, "CPU 1", 2000, NULL, 1, &Core1T, 1);
  
}

void NetworkHandle(void * pr){


  Serial.println("Conectando ao WiFi...");
  WiFi.begin(ssid, wifi_password); // Conecta ao WiFi designado
  while (WiFi.status() != WL_CONNECTED){ delay(300); }
  Serial.println("Conectado!");
  
  while (true){
    delay(300);
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
  
  while (true){
    peso = scale.get_units(10);

    Serial.print("Peso da prateleira: "); Serial.println(peso, 5);
    delay(10);
  }
  
}

void loop() {
  delay(1);
}
