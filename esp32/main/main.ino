#include "HX711.h"
#include <WiFiManager.h> /* https://github.com/tzapu/WiFiManager */
#include <WiFi.h>
#include <DNSServer.h>
#include <WebServer.h>
#include <HTTPClient.h> /* https://github.com/espressif/arduino-esp32/tree/master/libraries/HTTPClient */
#include <string>
#include <Arduino_JSON.h> /* https://github.com/arduino-libraries/Arduino_JSON */

#define DT 33
#define SCK 32

// 2. Adjustment settings
const long LOADCELL_OFFSET = 50682624;
const long LOADCELL_DIVIDER = 5895655;
const char *URL_AWS = "URL do AWS";



TaskHandle_t Core0T;
TaskHandle_t Core1T;

bool shouldSaveConfig = false;
HX711 scale;
float peso;
WiFiServer server(80);
WiFiManager wifiManager;
WiFiClient wclient;

const float desvio=0.000015;
void setup() {
  // put your setup code here, to run once:

  Serial.begin(9600);

  xTaskCreatePinnedToCore(NetworkHandle, "CPU 0", 5200, NULL, 1, &Core0T, 0);
  xTaskCreatePinnedToCore(SensorHandle, "CPU 1", 2000, NULL, 1, &Core1T, 1);
  
}

void NetworkHandle(void * pr){

  wifiManager.resetSettings();

  PORTAL:{
    //Modo de configuração do WiFi (Roteia uma rede)
    wifiManager.setAPCallback(configModeCallback);
    wifiManager.setSaveConfigCallback(saveConfigCallback);
    
    PORTAL_CONNECT:{
      if(!wifiManager.startConfigPortal("Estoque_Inteligente")){
        Serial.println("Ops, falhou ao criar o portal!");
        delay(2000);
        goto PORTAL_CONNECT;
      }else{
        Serial.println("WiFi salvo!"); 
      }
    }
  }

  int code;
  while (true){
   
    if(WiFi.status() == WL_CONNECTED){
      enviarDados(wclient);
    }else if (WiFi.status() == WL_CONNECTION_LOST){
      wifiManager.autoConnect();
      Serial.println("Conexão caiu! Reconectando...");
      delay(900);
    }else{
      goto PORTAL;
    }
    
    delay(1000);

  }

}

void enviarDados(WiFiClient c){
   int code;
   JSONVar json;
   HTTPClient http;
   
   http.begin(c, URL_AWS);
   json["peso"]=peso;
   
   code = http.POST(JSON.stringify(json));
   if(code !=0){
    Serial.printf("POST falhou. Erro: %s\n", http.errorToString(code).c_str());
   }
   
   http.end();
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

void configModeCallback (WiFiManager *myWiFiManager) {
  Serial.print("IP do portal: ");
  Serial.println(WiFi.softAPIP());

  Serial.println(myWiFiManager->getConfigPortalSSID());
}

void saveConfigCallback () {
  Serial.println("Salvando configuração do WiFi...");
  shouldSaveConfig = true;
}
