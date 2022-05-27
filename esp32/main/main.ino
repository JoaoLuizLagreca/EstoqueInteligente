#include "HX711.h"
#include <WiFi.h>
#include <string>

#define DT 33
#define SCK 32

const char* ssid = "WiFi ESP32";
const char* wifi_password = "44692324"; // Método prototipal, em um modelo de lançamento, o produto deveria apresentar uma interface de configuração para conectar à uma rede

// 2. Adjustment settings
const long LOADCELL_OFFSET = 50682624;
const long LOADCELL_DIVIDER = 5895655;



TaskHandle_t Core0T;
TaskHandle_t Core1T;

HX711 scale;
float peso;
WiFiServer server(80);

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
  Serial.print("Endereço IP: "); Serial.println(WiFi.localIP());

  server.begin();

  WiFiClient client;
  float pe;
  while (true){

    client = server.available();
    if(client){

      while(client.available()){
        client.read(); //Leia tudo para evitar colisão
      }
      pe = peso;
      
      client.println("HTTP/1.1 200 OK");
      client.println("Content-Type: application/json");
      client.println("Connection: close");
      client.println();

      client.println("{");
      client.println("\"peso\":"+String(pe));
      client.println("}");
    }
    
    delay(100);
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
  Serial.println("Tarado!");
  
  while (true){
    peso = scale.get_units(10);

    //Serial.print("Peso da prateleira: "); Serial.println(peso, 5);
    delay(10);
  }
  
}

void loop() {
  delay(1);
}
